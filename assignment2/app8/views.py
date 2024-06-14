from django.shortcuts import render
from .forms import MessageForm
from .utils import encode_message

def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            date = form.cleaned_data['date']
            encoded_message = encode_message(message, date)
            return render(request, 'app8/result.html', {'encoded_message': encoded_message})
    else:
        form = MessageForm()
    return render(request, 'app8/index.html', {'form': form})

def result(request):
    return render(request, 'app8/result.html')
