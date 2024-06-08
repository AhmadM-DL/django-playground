from django.urls import path
from .views import CreateDepatmentView, CreateEmployeeView

urlpatterns = [
    path('department/', CreateDepatmentView.as_view()),
    path('employee/', CreateEmployeeView.as_view()),
]