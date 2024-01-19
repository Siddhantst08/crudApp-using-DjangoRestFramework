from django.shortcuts import render

from rest_framework import generics
from .models import Section, Student
from .serializers import SectionSerializer, StudentSerializer
# Create your views here.

def index(request):
    return render(request, 'index.html')

class SectionList(generics.ListCreateAPIView):
    serializer_class = SectionSerializer

    def get_queryset(self):
        queryset = Section.objects.all()
        student = self.request.query_params.get('student')
        if student is not None:
            queryset = queryset.filter(student = student)
        return queryset
        
class SectionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SectionSerializer
    queryset = Section.objects.all()

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()




    
