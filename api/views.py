from django.shortcuts import render
from rest_framework import generics, status
from rest_framework import response
from .models import *
from .serializers import StudentSerializer


class StudentListCreate (generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self,request, *args, **kwargs ):
        Student.objects.all().delete()
        return response(status = status.HTTP_204_NO_CONTENT)
    
class StudentRetrieveUpdateDestroy(generics.RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "pk"


# Create your views here.
