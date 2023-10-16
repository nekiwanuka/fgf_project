# from rest_framework.authentication import BaseAuthentication
# from auth_app import exceptions
# from django.contrib.auth.models import User
# import firebase_admin
# from firebase_admin import credentials, auth
# from django.conf import settings


# default_app = firebase_admin.initialize_app(cred)
# """FIREBASE AUTHENTICATION"""
# class FirebaseAuthentication(BaseAuthentication):
#     """override authenticate method and write our custom firebase authentication."""
#     def authenticate(self, request):
#         """Get the authorization Token, It raise exception when no authorization Token is given"""
#         auth_header = request.META.get("HTTP_AUTHORIZATION")
#         if not auth_header:
#             raise exceptions.NoAuthToken("No auth token provided")
#         #Decoding the Token It rasie exception when decode failed.
#         id_token = auth_header.split(" ").pop()
#         decoded_token = None
#         try:
#             decoded_token = auth.verify_id_token(id_token)
#         except Exception:
#             raise exceptions.InvalidAuthToken("Invalid auth token")
                
#         """Return Nothing"""
#         if not id_token or not decoded_token:
#             return None
#         """Get the uid of an user"""
#         try:
#             uid = decoded_token.get("uid")
#         except Exception:
#             raise exceptions.FirebaseError()
#         """Get or create the user"""
#         user, created = User.objects.get_or_create(username=uid)
#         return (user, None)