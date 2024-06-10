from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers import UserSerializer, PasswordSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from .models import Password


class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginUserView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({}, status=status.HTTP_201_CREATED)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

class LogoutUserView(APIView):
    def post(self, request):
        logout(request)
        return Response({}, status=status.HTTP_201_CREATED)
               
class PasswordListCreateView(generics.ListCreateAPIView):
    serializer_class = PasswordSerializer
    queryset = Password.objects.all()
    permission_classes = [IsAuthenticated]