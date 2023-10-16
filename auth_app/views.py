from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User, Administrator, Contributor
from .serializers import UserSerializer, AdministratorSerializer, ContributorSerializer

#from rest_framework_simplejwt.views import TokenObtainPairView

#from django.shortcuts import render
#from pyrebase import pyrebase 
#from django.conf import settings

#from rest_framework.permissions import IsAuthenticated
#from auth_app.authentication import FirebaseAuthentication
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status

class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AdministratorListCreateView(ListCreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer

class AdministratorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer

class ContributorListCreateView(ListCreateAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

class ContributorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

""" 
class MyTokenObtainPairView(TokenObtainPairView):
    pass


class UserAPIView(APIView):
    permission_classes = [ IsAuthenticated ]
    #Here just add FirebaseAuthentication class in authentication_classes
    authentication_classes = [ FirebaseAuthentication ]
    def get(self,request):
            data = User.objects.all()
            serializer = UserSerializer(data, many = True)
            response = {
                   "status": status.HTTP_200_OK,
                   "message": "success",
                   "data": serializer.data
                   }
            return Response(response, status = status.HTTP_200_OK)



# Initialising database,auth and firebase for further use 
firebase=pyrebase.initialize_app(settings.config)
authe = firebase.auth()
database=firebase.database()
 
def signIn(request):
    return render(request,"Login.html")
def home(request):
    return render(request,"Home.html")
 
def postsignIn(request):
    email=request.POST.get('email')
    pasw=request.POST.get('pass')
    try:
        # if there is no error then signin the user with given email and password
        user=authe.sign_in_with_email_and_password(email,pasw)
    except:
        message="Invalid Credentials!!Please ChecK your Data"
        return render(request,"Login.html",{"message":message})
    session_id=user['idToken']
    request.session['uid']=str(session_id)
    return render(request,"Home.html",{"email":email})
 
def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request,"Login.html")
 
def signUp(request):
    return render(request,"Registration.html")
 
def postsignUp(request):
     email = request.POST.get('email')
     passs = request.POST.get('pass')
     name = request.POST.get('name')
     try:
        # creating a user with the given email and password
        user=authe.create_user_with_email_and_password(email,passs)
        uid = user['localId']
        idtoken = request.session['uid']
        print(uid)
     except:
        return render(request, "Registration.html")
     return render(request,"Login.html") """