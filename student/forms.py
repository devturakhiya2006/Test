from django import forms
from student.models import student ,Course

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'email', 'mobile', 'city']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_code', 'start_date', 'end_date', 'faculty_name', 'is_active']