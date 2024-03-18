from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('api/posts', views.PostList.as_view()),
    path('api/posts/<slug:slug>', views.PostDetails.as_view()),
    path('api/authors', views.AuthorList.as_view()),
    path('api/authors/<slug:slug>', views.AuthorDetails.as_view()),
    path('', views.landing, name='landing'),
]
