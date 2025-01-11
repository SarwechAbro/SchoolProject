from django.urls import path
from . import views


urlpatterns = [
    path('teacherapi/', views.TeacherAPI.as_view(), name='teacherapi'),
    path('teacherapi/<int:pk>/', views.TeacherDetailAPI.as_view(), name='teacherapi_detail'),

    path('studentapi/', views.StudentAPI.as_view(), name='studentapi'),
    path('studentapi/<int:pk>/', views.StudentDetailAPI.as_view(), name='studentapi_detail'),

    path('classapi/', views.ClassAPI.as_view(), name='classapi'),
    path('classapi/<int:pk>/', views.ClassDetailAPI.as_view(), name='classapi_detail'),

    path('chapterapi/', views.ChapterAPI.as_view(), name='chapterapi'),
    path('chapterapi/<int:pk>/', views.ChapterDetailAPI.as_view(), name='chapterapi_detail'),

    path('lectureapi/', views.LectureAPI.as_view(), name='lectureapi'),
    path('lectureapi/<int:pk>/', views.LectureDetailAPI.as_view(), name='lectureapi_detail'),

    path('courseapi/', views.CourseAPI.as_view(), name='courseapi'),
    path('courseapi/<int:pk>/', views.CourseDetailAPI.as_view(), name='courseapi_detail'),
]
