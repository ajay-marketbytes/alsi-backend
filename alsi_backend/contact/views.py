from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import EmailMessage
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

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error listing contact forms: {str(e)}", exc_info=True)
            return Response({
                'error': f'Failed to retrieve contact forms: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            contact_form = self.get_object()
            serializer = self.get_serializer(contact_form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ContactForm.DoesNotExist:
            return Response({'error': 'Contact form not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error retrieving contact form: {str(e)}", exc_info=True)
            return Response({
                'error': f'Failed to retrieve contact form: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            referer_url = request.META.get('HTTP_REFERER', '')
            submitted_url = "https://alsiglobal.com/contact_us/"
            data = request.data.copy()
            data.update({'referer_url': referer_url, 'submitted_url': submitted_url})

            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                logger.info("Serializer is valid, saving contact form")
                contact = serializer.save()
                logger.info("Contact form saved, sending emails")
                self._send_confirmation_email(contact)
                self._send_email_notification(contact)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.error(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating contact form: {str(e)}", exc_info=True)
            return Response({
                'error': f'Failed to submit form: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            contact_form = self.get_object()
            contact_name = contact_form.name
            contact_form.delete()
            return Response({
                'status': f'Message from {contact_name} deleted successfully'
            }, status=status.HTTP_200_OK)
        except ContactForm.DoesNotExist:
            return Response({'error': 'Contact form not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error deleting contact form: {str(e)}", exc_info=True)
            return Response({
                'error': f'Failed to delete message: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _send_confirmation_email(self, contact):
        try:
            subject = "Your Contact Form Submission was Successful"
            message = (
                f"Hello {contact.name},\n\n"
                f"Thank you for getting in touch with us. Your message has been successfully received.\n"
                f"Our team will review your submission and get back to you soon.\n\n"
                f"Details:\n"
                f"Name: {contact.name}\n"
                f"Email: {contact.email}\n"
                f"Phone: {contact.phone}\n"
                f"Message: {contact.message}\n"
            )
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[contact.email],
            )
            logger.info(f"Sending confirmation email to {contact.email}")
            email.send(fail_silently=False)
            logger.info("Confirmation email sent successfully")
        except Exception as e:
            logger.error(f"Failed to send confirmation email: {str(e)}", exc_info=True)

    def _send_email_notification(self, contact):
        try:
            subject = f"New Contact Form Submission from {contact.name}"
            message = (
                f"A new contact form submission:\n\n"
                f"Name: {contact.name}\n"
                f"Email: {contact.email}\n"
                f"Phone: {contact.phone}\n"
                f"Message: {contact.message}\n"
                f"Referer URL: {contact.referer_url}\n"
                f"Submitted URL: {contact.submitted_url}\n"
            )

            recipients = [
                'alsiglobalofficial@gmail.com',
               
            ]
            bcc_list = ['ajay@marketbytes.in', 'bcc2@example.com','silviathomas2000@gmail.com']
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=recipients,
                bcc=bcc_list,
            )
            logger.info(f"Sending notification email to {recipients}")
            email.send(fail_silently=False)
            logger.info("Notification email sent successfully")
        except Exception as e:
            logger.error(f"Failed to send notification email: {str(e)}", exc_info=True)
