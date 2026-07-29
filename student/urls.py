from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('contact/', views.contact, name='contact'),

 path('student/', views.student_list, name='student_list'),
 path('student/add/', views.student_add, name='student_add'), # <-- Fixed name
 path('student/edit/<int:pk>/', views.student_edit, name='student_edit'),
 path('student/delete/<int:pk>/', views.student_delete, name='student_delete'),

 path('Attendance/', views.AttendanceView, name='Attendance'),
]