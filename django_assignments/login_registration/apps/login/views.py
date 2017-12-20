from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.core.exceptions import ObjectDoesNotExist
import bcrypt

def index(request):
    return render(request, "register.html")

def create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password =  request.POST['password']
    passwordconf =  request.POST['passwordconf']
    if password == passwordconf:
        hash1 = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
        bcrypt.checkpw('password'.encode(), hash1)
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)    
        request.session['user'] = user.id
        return redirect("/success")
    else:
        return HttpResponse("Passwords don't match, hit the back button and refresh the page to try that again")

def success(request):
    user = User.objects.get(id = request.session['user'])
    context = {
        'user': user
    }
    return render(request, "success.html", context)

def loginsuccess(request):
    try:
         User.objects.get(email = request.POST['email'])
    except ObjectDoesNotExist:
        return HttpResponse("Email does not exist")
    else:
        user = User.objects.get(email = request.POST['email'])
        if request.POST['password'] == user.password:
            context = {
                'user': user
            }
            return render(request, "successful_login.html", context)
        else:
            return HttpResponse("password is invalid")