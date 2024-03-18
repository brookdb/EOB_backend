from django.views import generic
import django_filters
from rest_framework import  generics, permissions, filters
from .models import Post, Author
from .serializers import PostSerializer, AuthorSerializer
from .pagination import StandardResultsSetPagination
from django.shortcuts import render


def landing(request):
    return render(request, 'landing.html')

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination
    filterset_fields = ['author', 'status', 'created_on']
    search_fields = ['title', 'author__name']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    ordering_fields = ['created_on', 'title', 'author__name']
    ordering=['-created_on', 'title']

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

class AuthorList(generics.ListAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer
  pagination_class = StandardResultsSetPagination
  filterset_fields = ['slug','name']
  search_fields = ['slug','name']
  filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
  ordering_fields = ['name']
  ordering=[ 'name']

class AuthorDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer
  lookup_field = 'slug'