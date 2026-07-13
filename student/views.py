
# from django.http import HttpResponse

# def home(request): 
#     return HttpResponse("<h1>Hello, this is the student view.<h1>")

from django.shortcuts import render
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
