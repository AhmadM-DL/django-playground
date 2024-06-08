from rest_framework import generics
from .serializers import UserSerializer, PasswordSerializer, CreatePasswordSerializer
from .models import Password

class UserCreateView(generics.CreateAPIView):
    serializer_class= UserSerializer

class PasswordCreateView(generics.CreateAPIView):
    serializer_class = CreatePasswordSerializer

# Just for educational purpuse
# We dont use users id as a url variable usually
class PasswordListView(generics.ListAPIView):
    serializer_class = PasswordSerializer
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Password.objects.filter(user=user_id)