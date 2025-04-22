from .models import Teacher, Student, Class, Course, Chapter, Lecture
from .serializers import CourseSerializer , TeacherSerializer, StudentSerializer, ClassSerializer, ChapterSerializer, LectureSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


#Teacher APIs
@method_decorator(csrf_exempt, name='dispatch')
class TeacherAPI(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


@method_decorator(csrf_exempt, name='dispatch')
class TeacherDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'pk'



#Student APIs
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
 
   
@method_decorator(csrf_exempt, name='dispatch')
class StudentDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'pk'



#Class APIs
@method_decorator(csrf_exempt, name='dispatch')
class ClassAPI(ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


@method_decorator(csrf_exempt, name='dispatch')
class ClassDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'pk'



#Course APIs
@method_decorator(csrf_exempt, name='dispatch')
class CourseAPI(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
 

@method_decorator(csrf_exempt, name='dispatch')
class CourseDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'pk'

   

#Chapter APIs
@method_decorator(csrf_exempt, name='dispatch')
class ChapterAPI(ListCreateAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


@method_decorator(csrf_exempt, name='dispatch')
class ChapterDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    lookup_field = 'pk'

   

#Lecture APIs
@method_decorator(csrf_exempt, name='dispatch')
class LectureAPI(ListCreateAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


@method_decorator(csrf_exempt, name='dispatch')
class LectureDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    lookup_field = 'pk'

    

