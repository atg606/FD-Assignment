
from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        college = request.POST.get('college')
        course = request.POST.get('course')
        registration = Registration(name=name, college=college, course=course)
        registration.save()
        return HttpResponse('Registration successful')
    return render(request, 'app5/index.html')