from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactBanner, ContactForm
from .serializers import ContactBannerSerializer, ContactFormSerializer
import logging

logger = logging.getLogger(__name__)

class ContactBannerViewSet(viewsets.ModelViewSet):
    queryset = ContactBanner.objects.all()
    serializer_class = ContactBannerSerializer
    permission_classes = [AllowAny]

class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        referer_url = request.META.get('HTTP_REFERER', '')
        submitted_url = request.build_absolute_uri()
        data = request.data.copy()
        data.update({'referer_url': referer_url, 'submitted_url': submitted_url})

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        contact = serializer.save()

        try:
            # Send confirmation email to the user
            self._send_confirmation_email(contact)
            # Send notification email to the client or admin
            self._send_email_notification(contact)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Email sending failed: {str(e)}", exc_info=True)
            return Response({'error': 'Form submitted, but email notification failed.'},
                            status=status.HTTP_201_CREATED)

    def _send_confirmation_email(self, contact):
        subject = "Your Form Submission was Successful"
        message = (
            f"Hello {contact.name},\n\n"
            f"Thank you for contacting us. Your form has been successfully submitted.\n"
            f"Our team will review your submission and get back to you soon.\n\n"
            f"Here are the details of your submission:\n"
            f"Name: {contact.name}\n"
            f"Email: {contact.email}\n"
            f"Phone: {contact.phone}\n"
            f"Message: {contact.message}\n\n"
            f"Thank you for your patience!"
        )

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [contact.email],
        )

    def _send_email_notification(self, contact):
        subject = f"New Contact Form Submission from {contact.name}"
        message = (
            f"Hello,\n\n"
            f"A new contact form has been submitted.\n\n"
            f"Here are the details:\n"
            f"Name: {contact.name}\n"
            f"Email: {contact.email}\n"
            f"Phone: {contact.phone}\n"
            f"Message: {contact.message}\n"
            f"Referer URL: {contact.referer_url}\n"
            f"Submitted URL: {contact.submitted_url}\n\n"
            f"Please review and take necessary action."
        )

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [settings.CLIENT_EMAIL],
        )

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        try:
            ContactForm.objects.all().delete()
            return Response({'status': 'All messages deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error deleting all contact forms: {str(e)}", exc_info=True)
            return Response({'status': f'Failed to delete messages: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            contact_form = self.get_object()
            contact_form.delete()
            return Response({'status': 'Message deleted successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error deleting contact form: {str(e)}", exc_info=True)
            return Response({'status': f'Failed to delete message: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
