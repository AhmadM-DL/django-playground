from django.urls import path
from . import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [

    # User
    path('register/', views.RegisterUserView.as_view()),
    path('login/', views.LoginUserView.as_view()),
    path('logout/', views.LogoutUserView.as_view()),

    # API
    path("password/", views.PasswordListCreateView.as_view()),
]
