
from django.shortcuts import render
import itertools

def perm(word):
    return [''.join(p) for p in itertools.permutations(word)]

def home(request):
    permutations = {}
    if request.method == 'POST':
        word3 = request.POST.get('word3')
        word4 = request.POST.get('word4')
        word5 = request.POST.get('word5')
        if word3:
            permutations['word3'] = perm(word3)
        if word4:
            permutations['word4'] = perm(word4)
        if word5:
            permutations['word5'] = perm(word5)
    return render(request, 'app4/index.html', {
        'permutations': permutations
    })