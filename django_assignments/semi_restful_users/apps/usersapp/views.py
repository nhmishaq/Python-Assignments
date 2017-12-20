from django.shortcuts import render, HttpResponse, redirect
from models import User

def index(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, "index.html", context)

def users_new(request):
    return render(request, "new.html")

def edit(request, userid):
    user = User.objects.get(id=userid)
    context = {
        'user': user
    }
    return render(request, "edit.html", context)

def show(request, userid):
    user = User.objects.get(id=userid)
    context = {
        'user': user
    }
    return render(request, "show.html", context)

def create(request):
    name = request.POST['name']
    email = request.POST['email']  
    User.objects.create(name=name, email=email)    
    return redirect("/users/")

def destroy(request, userid):
    # gone = User.objects.get(id=userid)
    # print user.name
    # gone.delete()
    # print user.name
    # user.save()
    user = User.objects.get(id=userid)
    user.delete()

    return redirect("/users/")

def update(request, userid):
    user = User.objects.get(id=userid)
    user.name = request.POST.get('name', "")
    user.email = request.POST.get('email', "")
    # print user.email
    user.save()
    # print user.email
    return redirect("/users/")