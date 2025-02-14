from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from .models import CareersBanner, CareersForm
from django.core.mail import EmailMessage
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CareersBannerSerializer, CareersFormSerializer
from django.conf import settings
from django.template.loader import render_to_string
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

    def create(self, request, *args, **kwargs):
        referer_url = request.META.get('HTTP_REFERER', '')
        submitted_url = request.build_absolute_uri()
        data = request.data.copy()
        data.update({'referer_url': referer_url, 'submitted_url': submitted_url})

        if 'file' not in request.FILES:
            return Response({'error': 'File is required'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        career = serializer.save(file=request.FILES['file'])

        try:
            self._send_email_notification(career, request.FILES['file'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Email sending failed: {str(e)}", exc_info=True)
            return Response({'error': 'Form submitted, but email notification failed.'},
                            status=status.HTTP_201_CREATED)

    def _send_email_notification(self, career, file):
        subject = f"New Career Form Submission from {career.name}"
        context = {
            'name': career.name,
            'email': career.email,
            'phone': career.phone,
            'message': career.message,
            'referer_url': career.referer_url,
            'submitted_url': career.submitted_url
        }
        html_message = render_to_string('emails/careers_form.html', context)

        email = EmailMessage(
            subject=subject,
            body=html_message,
            from_email=settings.CAREERS_EMAIL_HOST_USER,
            to=[settings.CAREERS_EMAIL_HOST_USER],
        )
        email.content_subtype = "html"

        if file:
            email.attach(file.name, file.read(), file.content_type)

        email.send()

    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        try:
            CareersForm.objects.all().delete()
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
