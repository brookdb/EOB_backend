from rest_framework import serializers
from .models import Post, Author


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Post
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'slug', 'bio', 'avatar']
        lookup_field = 'slug'
