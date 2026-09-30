
# from django.http import HttpResponse

# def home(request): 
#     return HttpResponse("<h1>Hello, this is the student view.<h1>")

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Attendance, Course, Dept, student
from django import forms
from .forms import StudentForm
from .forms import CourseForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.http import JsonResponse

@login_required
def home(request):
    data = {
    'name':'Dev',
    'course':'Django',
    'collage':'JG University',
    }
    subject=["Django","Agile","Angular","BigData"]
    return render(request, 'index.html', {'data': data, 'subject': subject,'Marks':60})
@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

@login_required
def student_list(request):
    students = student.objects.all()
    return render(request, 'student_crud/list.html', {'students': students})



# def student_add(request):
#     if request.method == 'POST':
#         # name = request.POST.get('name')
#         # email = request.POST.get('email')
#         # mobile = request.POST.get('mobile')
#         # city = request.POST.get('city')
        
#         student.objects.create(
#             name=request.POST ['name'],
#             email=request.POST ['email'], 
#             mobile=request.POST ['mobile'], 
#             city=request.POST ['city'],)
#         return redirect('student_list')
        
#     return render(request, 'student_crud/add.html')

@login_required
def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_crud/add.html', {'form': form})
        

# --- UPDATE: Edit  an existing student ---
@login_required
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



# --- DELETE: Remove a student ---
@login_required
def student_delete(request, pk):
    stud = get_object_or_404(student, pk=pk)
    stud.delete()
    return redirect('student_list')

@login_required
def AttendanceView(request):
    attendance_list = Attendance.objects.all()
    return render(request, 'student_crud/Attendence.html', {'attendences': attendance_list})


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'Course_crud/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'Course_crud/course_list.html'
    context_object_name = 'courses'

class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model=Course
    fields='__all__'
    template_name='Course_crud/course_form.html'
    success_url=reverse_lazy('course_list')

class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model=Course
    template_name='Course_crud/course_confirm_delete.html'
    success_url=reverse_lazy('course_list')

class CourseDetailsView(LoginRequiredMixin, DetailView):
    model=Course
    template_name='Course_crud/course_details.html'

# def dept_list(request):
#    departments = Dept.objects.all()
#    return render(request, 'Dept/Dept_list.html', {'dept': departments})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect('home')
        return render(request, 'Course_crud/login.html',
                      {'error': 'Invalid username or password'})

    return render(request, 'Course_crud/login.html')

def logout_view(request):
    logout(request)
    request.session.flush() 
    return redirect('login')

def ajax_demo(request):
    name = request.GET.get("name", "")
    return JsonResponse({
        "message": "Hello "+name + "! Ajax is working."
    })