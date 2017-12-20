from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "placeholder to display all the surveys created"
    return HttpResponse(response)

def new(request):
    brown = "placeholder to display a new form to create a new blog"
    return HttpResponse(brown)
