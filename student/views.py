
# from django.http import HttpResponse

# def home(request): 
#     return HttpResponse("<h1>Hello, this is the student view.<h1>")

from django.shortcuts import get_object_or_404, redirect, render
from .models import Attendance, student

def home(request):
    data = {
    'name':'Dev',
    'course':'Django',
    'collage':'JG University',
    }
    subject=["Django","Agile","Angular","BigData"]
    return render(request, 'index.html', {'data': data, 'subject': subject,'Marks':60})
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def student_list(request):
    students = student.objects.all()
    return render(request, 'student_crud/list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        # name = request.POST.get('name')
        # email = request.POST.get('email')
        # mobile = request.POST.get('mobile')
        # city = request.POST.get('city')
        
        student.objects.create(
            name=request.POST ['name'],
            email=request.POST ['email'], 
            mobile=request.POST ['mobile'], 
            city=request.POST ['city'],)
        return redirect('student_list')
        
    return render(request, 'student_crud/add.html')

# --- UPDATE: Edit  an existing student ---
def student_edit(request, pk):
    stud = get_object_or_404(student, pk=pk)
    
    if request.method == 'POST':
        stud.name = request.POST.get('name')
        stud.email = request.POST.get('email')
        stud.mobile = request.POST.get('mobile')
        stud.city = request.POST.get('city')
        stud.save()
        return redirect('student_list')
        
    return render(request, 'student_crud/edit.html', {'student': stud})


def AttendanceView(request):
    attendance_list = Attendance.objects.all()
    return render(request, 'student_crud/Attendence.html', {'attendences': attendance_list})











# --- DELETE: Remove a student ---
def student_delete(request, pk):
    stud = get_object_or_404(student, pk=pk)
    stud.delete()
    return redirect('student_list')