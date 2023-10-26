from business_logic.utilities.constants import API_DOMAIN
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from core.utilities.mailing import EmailSender
from business_logic.management.user_management import UserManager


class EmailVerificationLinkSender:

    def __init__(self, request):
        self.request = request
        self.email = request.data['email']

    def _send(self):

        user = UserManager().get_list().filter(email=self.email)[0]
        email = user.email
        token = RefreshToken.for_user(user)
        relative_link = reverse('verify-email')
        absurl = API_DOMAIN+relative_link+'?token='+str(token)
        email_body = 'Hi '+email+' You are almost done with your registration process with the Medihub Platform.\n\
        Please follow the link below to verify your email and activate your medihub account.\n' \
                 + absurl
        data = {
            'email_subject': 'Email Verification and Account Activation',
            'to_email': email,
            'email_body': email_body
        }
        EmailSender.send_email(data)

        response_data = {
            'email': email,
            'registration_status': 'success',
            'message': 'Email verification link has been sent to this email (' + email + ')'
        }
        return Response(data=response_data, status=status.HTTP_201_CREATED)

    def __send(self, email_to_be_verified):
        user = self.request.user
        email = (str(email_to_be_verified)).lower()
        token = RefreshToken.for_user(user)
        relative_link = reverse('verify-user-email')
        absurl = API_DOMAIN+relative_link+'?email='+email+'&token='+str(token)
        email_body = 'Hi, '+email+', you requested to add this email to your medihub profile.\n\
        Please click the link below to verify this email if you recognize this request.\n' \
                 + absurl
        data = {
            'email_subject': 'Email Verification',
            'to_email': email,
            'email_body': email_body
        }
        EmailSender.send_email(data)

        response_data = {
            'email': email,
            'registration_status': 'success',
            'message': 'Email verification link has been sent to this email (' + email + ')'
        }
        return Response(data=response_data, status=status.HTTP_201_CREATED)

    def send(self):
        return self._send()

    def send_link(self, to_email):
        return self.__send(to_email)
