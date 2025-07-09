from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status, permissions

from .serializers import CustomUserLoginSerializer, CustomUserRegisterSerializer, UserProfileSerializer, CommentsSerializer
from .models import CustomUser, Comment


# User Registration: APIView
# User Logout: APIView
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
    

class UserLogOutAPIView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'detail': "Logged Out."}, status=status.HTTP_200_OK)
    

class UserProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = self.request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    

class UserCommentsAPIView(APIView):
    permission_classes = []
    def get(self, request):
        comments = Comment.objects.filter(author=self.request.user)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

 