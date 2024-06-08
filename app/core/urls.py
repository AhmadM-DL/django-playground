from django.urls import path
from . import views

urlpatterns = [
    path('create_user', views.CreateUserProfileView.as_view(), name='create_user'),
]