from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import EmailMessage
from django.conf import settings
import requests
import logging
from models import ContactBanner,ContactForm
from serializers import ContactBannerSerializer,ContactFormSerializer
 
logger = logging.getLogger(__name__)
 
class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [AllowAny]
 
    def create(self, request, *args, **kwargs):
        try:
            # Extract reCAPTCHA token
            recaptcha_token = request.data.get("recaptcha_token")
            if not recaptcha_token:
                return Response({"error": "reCAPTCHA token missing"}, status=status.HTTP_400_BAD_REQUEST)
 
            # Verify reCAPTCHA v3 with Google
            recaptcha_response = requests.post(
                "https://www.google.com/recaptcha/api/siteverify",
                data={
                    "secret": settings.RECAPTCHA_PRIVATE_KEY,
                    "response": recaptcha_token,
                },
            ).json()
 
            if not recaptcha_response.get("success") or recaptcha_response.get("score", 0) < 0.5:
                logger.warning(f"reCAPTCHA verification failed: {recaptcha_response}")
                return Response({"error": "reCAPTCHA verification failed"}, status=status.HTTP_400_BAD_REQUEST)
 
            # Proceed with form data
            referer_url = request.META.get("HTTP_REFERER", "")
            submitted_url = "https://alsiglobal.com/contact-us/"
            data = request.data.copy()
            data.update({"referer_url": referer_url, "submitted_url": submitted_url})
 
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
            return Response({"error": f"Failed to submit form: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
    # Other methods (list, retrieve, destroy, _send_confirmation_email, _send_email_notification) remain unchanged
 
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
            recipients = ["alsiglobalofficial@gmail.com"]
            bcc_list = ["ajay@marketbytes.in", "silviathomas2000@gmail.com"]
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