from django.shortcuts import render
from rest_framework import generics
from .models import Course, Registration
from .serializers import CourseSeraializer, RegistrationSerializers
from rest_framework.permissions import AllowAny



# Create your views here.

class CourseListview(generics.ListAPIView):
    queryser = Course.objects.all()
    serializer_class = CourseSeraializer
    permission_classes = [AllowAny]  

class RegistrationCreateView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializers
    permission_classes = [AllowAny]