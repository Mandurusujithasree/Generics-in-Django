from django.shortcuts import render
from api.models import Course
from rest_framework.response import Response
from api.serializers import CourseSerializer
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics
# Create your views here.

class Course_list(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class Course_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer