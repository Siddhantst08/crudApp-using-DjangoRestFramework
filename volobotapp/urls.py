from django.contrib import admin
from django.urls import path, include
from .views import SectionList, SectionDetail, StudentList, StudentDetail
from . import views

urlpatterns = [
    path('section/', SectionList.as_view()),
    path('section/<int:pk>/', SectionDetail.as_view()),
    path('student/', StudentList.as_view()),
    path('student/<int:pk>/', StudentDetail.as_view()),
    path('', views.index, name = 'index')
]