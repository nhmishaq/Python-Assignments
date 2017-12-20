from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    return render(request, "form.html")

def generate(request):
    request.session['word'] = get_random_string(length=14)
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    return redirect('/')