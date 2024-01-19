from django.db import models

# Create your models here.


class Student(models.Model):
    studentName = models.CharField(max_length = 100, unique = True)
    studentGender = models.CharField(max_length =100)

    def __str__(self):
        return self.studentName

class Section(models.Model):
    studentSection = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete = models.CASCADE)

    def __str__(self):
        return self.studentSection



    
