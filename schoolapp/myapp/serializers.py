from rest_framework import serializers
from .models import Teacher, Student, Class, Course, Chapter, Lecture

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Teacher 
        fields = '__all__'        

class StudentSerializer(serializers.ModelSerializer):
    teacher_id = TeacherSerializer(many=True, read_only=True)
    
    class Meta:
        model = Student
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class_id = ClassSerializer(read_only=True)
    teacher_id = TeacherSerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = '__all__'        

class ChapterSerializer(serializers.ModelSerializer):
    course_id = CourseSerializer(read_only=True)
    
    class Meta:
        model = Chapter
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):    
    chapter_id = ChapterSerializer(many=True, read_only=True)
    
    class Meta:
        model = Lecture 
        fields = '__all__'