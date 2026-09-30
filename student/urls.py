from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .views import (
    CourseListView,
    CourseCreateView,
    CourseDetailsView,
    CourseUpdateView,
    CourseDeleteView
)

urlpatterns = [
 path("demo/",views.ajax_demo,name="demo"),

 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('contact/', views.contact, name='contact'),
 path('login/', views.login_view, name='login'),
 path('logout/', views.logout_view, name='logout'),

 path('course/list/', views.CourseListView.as_view(), name='course_list'),
 path('course/add/', views.CourseCreateView.as_view(), name='course_add'),
 path('course/<int:pk>/edit', views.CourseUpdateView.as_view(), name='course_update'),
 path('course/<int:pk>/delete', views.CourseDeleteView.as_view(), name='course_delete'),
 path('course/<int:pk>/', views.CourseDetailsView.as_view(), name='course_detail'),

 path('student/', views.student_list, name='student_list'),
 path('student/add/', views.student_add, name='student_add'), # <-- Fixed name
 path('student/edit/<int:id>/', views.student_edit, name='student_edit'),
 path('student/delete/<int:id>/', views.student_delete, name='student_delete'),

 path('Attendance/', views.AttendanceView, name='Attendance'),

  # path('dept/', views.dept_list, name='dept_list'),

]