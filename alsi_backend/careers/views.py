from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import EmailMessage
from django.conf import settings
from .models import CareersBanner, CareersForm
from .serializers import CareersBannerSerializer, CareersFormSerializer
import logging

logger = logging.getLogger(__name__)

class CareersBannerViewSet(viewsets.ModelViewSet):
    queryset = CareersBanner.objects.all()
    serializer_class = CareersBannerSerializer
    permission_classes = [AllowAny]

class CareersFormViewSet(viewsets.ModelViewSet):
    queryset = CareersForm.objects.all()
    serializer_class = CareersFormSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(f"Error listing career forms: {str(e)}", exc_info=True)
            return Response({
                'error': f'Failed to retrieve career forms: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            career_form = self.get_object()
            serializer = self.get_serializer(career_form)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CareersForm.DoesNotExist:
            return Response({'error': 'Career form not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error retrieving career form: {str(e)}", exc_info=True)
            return Response({
                'error': f'Failed to retrieve career form: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self, request, *args, **kwargs):
        try:
            referer_url = request.META.get('HTTP_REFERER', '')
            submitted_url = "https://alsiglobal.com/careers/"
            data = request.data.copy()
            data.update({'referer_url': referer_url, 'submitted_url': submitted_url})

            if 'file' not in request.FILES:
                return Response({'error': 'File is required'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                logger.info("Serializer is valid, saving career form")
                career = serializer.save(file=request.FILES['file'])
                logger.info("Career form saved, sending emails")
                self._send_confirmation_email(career)
                self._send_email_notification(career, request.FILES['file'])
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.error(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating career form: {str(e)}", exc_info=True)
            return Response({
                'error': f'Failed to submit form: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            career_form = self.get_object()
            career_name = career_form.name
            career_form.delete()
            return Response({
                'status': f'Message from {career_name} deleted successfully'
            }, status=status.HTTP_200_OK)
        except CareersForm.DoesNotExist:
            return Response({'error': 'Career form not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(f"Error deleting career form: {str(e)}", exc_info=True)
            return Response({
                'error': f'Failed to delete message: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def _send_confirmation_email(self, career):
        try:
            subject = "Your Career Form Submission was Successful"
            message = (
                f"Hello {career.name},\n\n"
                f"Thank you for submitting your career application. Your form has been successfully received.\n"
                f"Our team will review your submission and get back to you soon.\n\n"
                f"Details:\n"
                f"Name: {career.name}\n"
                f"Email: {career.email}\n"
                f"Phone: {career.phone}\n"
                f"Message: {career.message}\n"
            )
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[career.email],
            )
            logger.info(f"Sending confirmation email to {career.email}")
            email.send(fail_silently=False)
            logger.info("Confirmation email sent successfully")
        except Exception as e:
            logger.error(f"Failed to send confirmation email: {str(e)}", exc_info=True)

    def _send_email_notification(self, career, file):
        try:
            subject = f"New Career Form Submission from {career.name}"
            message = (
                f"A new career form submission:\n\n"
                f"Name: {career.name}\n"
                f"Email: {career.email}\n"
                f"Phone: {career.phone}\n"
                f"Message: {career.message}\n"
                f"Referer URL: {career.referer_url}\n"
                f"Submitted URL: {career.submitted_url}\n"
                f"File: See attached file or download from {career.file.url}\n"
            )
            recipients = [
                'alsiglobalofficial@gmail.com',  
            ]
            bcc_list = ['ajay@marketbytes.in','silviathomas2000@gmail.com']

            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=recipients,
                bcc=bcc_list,
            )
            if file:
                file.seek(0)
                email.attach(file.name, file.read(), file.content_type)
            logger.info(f"Sending notification email to {recipients}")
            email.send(fail_silently=False)
            logger.info("Notification email sent successfully")
        except Exception as e:
            logger.error(f"Failed to send notification email: {str(e)}", exc_info=True)
