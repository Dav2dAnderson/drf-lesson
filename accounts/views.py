from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from .serializers import CustomUserLoginSerializer, CustomUserRegisterSerializer

# User Registration: APIView
# Create your views here.


class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = CustomUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username'] # username = 'admin'
            password = serializer.validated_data['password'] # password = 'admin'

            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key})
            return Response({'detail': "Foydalanuvchi topilmadi."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors)
    

class UserRegisterAPIView(APIView):
    def post(self, request):
        serializer = CustomUserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()    
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "message": "User has been created.",
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    