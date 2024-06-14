from django.shortcuts import render
from .forms import AmountForm
from .utils import number_to_words

def index(request):
    if request.method == 'POST':
        form = AmountForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            words = number_to_words(amount)
            return render(request, 'app7/result.html', {'amount': amount, 'words': words})
    else:
        form = AmountForm()
    return render(request, 'app7/index.html', {'form': form})

def result(request):
    return render(request, 'app7/result.html')
