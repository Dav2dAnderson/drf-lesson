from rest_framework.serializers import ModelSerializer

from .models import Post, Article


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'summary', 'content']

