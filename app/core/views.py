from rest_framework import generics
from.serializers import DepartmentSerializer, EmployeeSerializer

class CreateDepatmentView(generics.CreateAPIView):
    serializer_class = DepartmentSerializer


class CreateEmployeeView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer
