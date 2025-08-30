from django.shortcuts import render
from rest_framework import generics
from .models import Course, Registration
from .serializers import CourseSeraializer, RegistrationSerializers



# Create your views here.

class CourseListview(generics.ListAPIView):
    queryser = Course.objects.all()
    serializer_class = CourseSeraializer
    

class RegistrationCreateView(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializers