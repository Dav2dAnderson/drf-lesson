from django.shortcuts import render

from rest_framework import views, viewsets, status, permissions
from rest_framework.response import Response

from .serializers import PostSerializer, ArticleSerializer
from .models import Post, Article
from .permissions import IsAdminOrReadOnly
# Create your views here.
"""Meta class short description | APIView: get, post"""

# APIView: get, post, put, patch, delete
# ViewSet: list, retrieve, create, destroy, update

# User Authentification: APIView, Token


class PostAPIView(views.APIView):
    def get(self, request, pk=None):
        if not pk:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        else:
            try:
                post = Post.objects.get(pk=pk)
                serializer = PostSerializer(post)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Post.DoesNotExist:
                return Response({'detail': "Ma'lumot topilmadi."}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages)
        
    def put(self, request, pk=None):
        if pk:
            try:
                post = Post.objects.get(pk=pk)
                serializer = PostSerializer(post, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except Post.DoesNotExist:
                return Response({'detail': "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'PUT metodi pk talab qiladi.'})
        
    def patch(self, request, pk=None):
        if pk:
            try:
                post = Post.objects.get(pk=pk)
                serializer = PostSerializer(post, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
            except Post.DoesNotExist:
                return Response({'detail': "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'PATCH method pk talab qiladi.'})
        
    def delete(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return Response({'detail': "O'chirildi."})
        except Post.DoesNotExist:
            return Response({'detail': "Ma'lumot topilmadi."}, status=status.HTTP_404_NOT_FOUND)
    


class ArticleViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly] # "," = and  "|" = or
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk):
        article = Article.objects.get(pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages)

    def destroy(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            article.delete()
            return Response({'detail': "O'chirildi."})
        except Article.DoesNotExist:
            return Response({'detail': "Ma'lumot topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        
    def update(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.error_messages)
        except Article.DoesNotExist:
            return Response({'detail': "Ma'lumot topilmadi"})
        
    