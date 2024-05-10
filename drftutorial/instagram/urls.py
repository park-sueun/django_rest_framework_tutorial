from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('posts/', views.PublicPostListView.as_view(), name='PublicPostListView'),
    path('posts/<int:pk>/', views.PostView.as_view(), name='PostView'),
]