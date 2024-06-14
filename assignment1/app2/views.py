from django.shortcuts import render
import math
# Create your views here.
def home(request):
    factorial=None
    if request.method=='POST':
        try:
            num = int(request.POST.get('number'))
            if 1 <= num <= 10:
                factorial = math.factorial(num)
            else:
                factorial = 'Number out of range'
        except ValueError:
            factorial = 'Invalid input'

    return render(request, 'app2/index.html', {'factorial': factorial})

