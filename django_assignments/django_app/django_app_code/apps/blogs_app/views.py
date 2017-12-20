from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    response = "hello"
    return HttpResponse(response)

def new(request):
    brown = "placeholder to display a new form to create a new blog"
    return HttpResponse(brown)

def create(request):
    fantastic = "placeholder to create a new form to create a new blog"
    return HttpResponse(fantastic)

def show(request, number):
    response = 'placeholder to show a blog ' + number
    return HttpResponse(response, number)

def edit(request, year):
    response = 'placeholder to edit blog year ' + year
    return HttpResponse(response)

def destroy(request):
    return redirect ('/')