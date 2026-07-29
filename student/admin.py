from django.contrib import admin
from .models import Attendance, student,Course

# Register your models here.
admin.site.register(Course)
admin.site.register(student)
admin.site.register(Attendance)