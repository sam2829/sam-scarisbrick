from django.shortcuts import render
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import ContactForm
import logging

logger = logging.getLogger(__name__)


class SendEmailView(APIView):
    """
    Class so user can send email
    """
    def post(self, request):
        form = ContactForm(request.data)
        # Check form is valid
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Construct the email content
            email_message = (
                f"Name: {name}\nEmail: {email}\n "
                f"Subject: {subject}\n\n{message}"
            )

            email = EmailMessage(
                subject=subject,
                body=email_message,
                to=['smscarisbrick1@gmail.com'],
            )

            try:
                email.send()
                return Response(
                    {'message': 'Email sent successfully'},
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                logger.error(f"Failed to send email: {e}")
                return Response(
                    {'error': str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response(
                {'errors': form.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
