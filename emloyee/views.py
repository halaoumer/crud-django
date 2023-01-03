from django.shortcuts import render

# Create your views here.


# Create your views here.
from django.shortcuts import render
from rest_framework import generics

from .serializers import EmployeeSerializer
from .models import Employee
# Create your views here.

class empList(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class empDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer