from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "form.html")

def result(request):
    return render(request, "results.html")

def submit(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comments'] = request.POST['comments']
    return redirect('/result')