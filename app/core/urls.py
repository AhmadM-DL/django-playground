from django.urls import path, re_path
from . import views

urlpatterns = [
    path('user/', views.UserCreateView.as_view()),
    path("password/", views.PasswordCreateView.as_view()),
    re_path("^password/(?P<user_id>.+)/$", views.PasswordListView.as_view())
]
