from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
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
            self._send_email_notification(contact)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Email sending failed: {str(e)}", exc_info=True)
            return Response({'error': 'Form submitted, but email notification failed.'},
                            status=status.HTTP_201_CREATED)

    def _send_email_notification(self, contact):
        subject = f"New Contact Form Submission from {contact.name}"
        context = {
            'name': contact.name,
            'email': contact.email,
            'phone': contact.phone,
            'message': contact.message,
            'referer_url': contact.referer_url,
            'submitted_url': contact.submitted_url
        }
        html_message = render_to_string('emails/contact_form.html', context)
        plain_message = render_to_string('emails/contact_form.txt', context)

        send_mail(
            subject,
            plain_message,
            settings.CONTACT_EMAIL_HOST_USER,
            [settings.CONTACT_EMAIL_HOST_USER],
            html_message=html_message,
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
