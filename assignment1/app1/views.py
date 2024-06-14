from django.shortcuts import render
import math

# Create your views here.
def home(request):
    n=5
    square=n*n
    factorial=math.factorial(n)
    return render (request,'app1/index.html',{'square': square, 'factorial':factorial} )
