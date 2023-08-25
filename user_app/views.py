from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Usr
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate



class Sign_up(APIView):

    def post(self,request):
        request.data["username"] = request.data["email"]
        new_user = Usr.objects.create_user(**request.data)
        token, created = Token.objects.get_or_create(user=new_user)
        return Response({'user':new_user.email, 'token':token.key}, HTTP_201_CREATED)
    

class Info(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    def get(self, request):
        return Response(request.user.email)
        


class Log_in(APIView):

    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(token.key)
        else:
            return Response('INVALID CREDENTIALS', status=HTTP_404_NOT_FOUND)

     
class Log_out(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print("here")
        request.user.auth_token.delete()  
        return Response(status=HTTP_204_NO_CONTENT)
    

class Admin_Sign_up(APIView):

    def post(self, request):
        request.data["username"] = request.data["email"]
        admin_user = Usr.objects.create_user(**request.data)
        admin_user.is_staff = True 
        admin_user.is_superuser = True 
        admin_user.save()
        return Response({'sign_up_admin':True}, status=HTTP_201_CREATED)      