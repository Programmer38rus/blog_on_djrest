from app.models import Post, Category, User
from rest_framework import serializers
# from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'bio')


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    category = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
        # fields = ('name', 'category')