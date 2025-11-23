from django.db import models


# Class Model
class Class(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    

# Course Model
class Course(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


# Teacher Model
class Teacher(models.Model):
    employee_id = models.IntegerField(default=0)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    class_id = models.ManyToManyField(Class, blank=True)
    course_id = models.ManyToManyField(Course, blank=True)
    def __str__(self):
        return self.name


# Student Model
class Student(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    teacher_id = models.ManyToManyField(Teacher, blank=True)
    class_id = models.ManyToManyField(Class, blank=True)
    def __str__(self):
        return self.name


# Chapter Model
class Chapter(models.Model):
    name = models.CharField(max_length=255)  
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, null=True,  blank=True) 
    def __str__(self):
        return self.name 


# Lecture Model
class Lecture(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='lectures/', blank=True, null=True)
    chapter_id = models.ManyToManyField(Chapter, blank=True)  
    def __str__(self):
        return self.name


    
        
