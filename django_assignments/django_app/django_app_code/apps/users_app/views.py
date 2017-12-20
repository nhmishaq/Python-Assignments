from django.shortcuts import render, HttpResponse, redirect

def index(request):
    response = "welcome users"
    return HttpResponse(response)

def register(request):
    brown = "placeholder for users to create a new user record"
    return HttpResponse(brown)

def login(request):
    fantastic = "placeholder for users to login"
    return HttpResponse(fantastic)

def users(request):
    fantastic = "placeholder to later display all the list of users"
    return HttpResponse(fantastic)