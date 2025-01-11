from django.contrib import admin

# Register your models here.
from .models import Teacher, Student, Class, Course, Chapter, Lecture

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'designation']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id','name']


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ['name', 'file']            


