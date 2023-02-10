from django.urls import path 
from .views import register
from . import views
from django.views.decorators.cache import cache_page 
urlpatterns = [
    path('register/', register, name='signup'),
     path('enroll', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    path('courses/',views.StudentCourseListView.as_view(),name='student_course_list'),
    path('course/<pk>/',cache_page(60*15)(views.StudentCourseDetailView.as_view()),name='student_course_detail'),
    path('course/<pk>/<module_id>/', cache_page(60*15)(views.StudentCourseDetailView.as_view()),name='student_course_detail_module'),
]