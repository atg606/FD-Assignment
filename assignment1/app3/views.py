from django.shortcuts import render
import math
# Create your views here.
def home(request):
    factorials = {i: math.factorial(i) for i in range(3, 9)}
    return render(request, 'app3/index.html', {
        'factorials': factorials})
    
