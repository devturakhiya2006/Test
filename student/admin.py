from django.contrib import admin
from .models import Attendance, Dept, student,Course

# Register your models here.
admin.site.register(Course)
admin.site.register(student)
admin.site.register(Attendance)
admin.site.register(Dept)