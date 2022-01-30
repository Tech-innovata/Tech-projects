from django.db import models

# Create your models here.
class Register(models.Model):
    surname=models.CharField(max_length=100)
    givenname=models.CharField(max_length=100)
    program=models.CharField(max_length=100)
    yearofstudy=models.CharField(max_length=100)
    formerschool=models.CharField(max_length=100)
    parent=models.CharField(max_length=100)
    

class Student(models.Model):
    Name=models.CharField(max_length=30)
    Students_no=models.TextField(default=1900727591)
    Reg_no=models.CharField(max_length=30)
    Paragraphs=models.TextField(max_length=500,null=True,blank=True)
