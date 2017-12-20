from django.shortcuts import render, HttpResponse, redirect
from models import User, Poke
from django.core.exceptions import ObjectDoesNotExist
import bcrypt
from django.db.models import Count

def index(request):
    request.session.clear()
    return render(request, "index.html")

def create(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password =  request.POST['password']
    passwordconf =  request.POST['passwordconf']
    birthday = request.POST['birthday']
    errors = User.objects.basic_validator(request.POST)
    if len (errors) :
        for tag, error in errors.iteritems():
            messages.error(request, error)            
        return redirect('/')
    
    if password == passwordconf:
        hash1 = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())
        bcrypt.checkpw('password'.encode(), hash1)
        user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password, birthday=birthday)    
        request.session['user'] = user.id
        return redirect("/success")
    else:
        return HttpResponse("Passwords don't match, hit the back button and refresh the page to try that again")

def success(request):
    user = User.objects.get(id = request.session['user'])
    context = {
        'user': user
    }
    return render(request, "dashboard.html", context)

def loginsuccess(request):
    try:
         User.objects.get(email = request.POST['email'])
    except ObjectDoesNotExist:
        return HttpResponse("Email does not exist")
    else:
        user = User.objects.get(email = request.POST['email'])
        user_list= User.objects.all()
        if request.POST['password'] == user.password:
            context = {
                'user': user
                'user_list': user_list            }
            return render(request, "successful_registration.html", context)
        else:
            return HttpResponse("password is invalid")

def poke(request, id):
    poker = Users.objects.get(id=request.session['id'])
    poked = Users.objects.get(id=id)
    poke = Poke()
    poke.poker = poker
    poke.poked = poked
    poke.counter = poke.counter + 1
    poke.save()
    return redirect('/success')

def user_dashboard(request):
    user = User.objects.get(id = request.session['user'])
    user_list = User.objects.all()
    pokes = Poke.objects.all()
    # countsum = Poke.objects.filter(pokeduser=request.session['user'])
    # poker_list = Poke.objects.filter(poked=request.session['user'].exclude(request.session['user']))
    # current_user = User.objects.get(id=request.session['id'])
    
    context = {
        'user_list': user_list
        # 'pokes': pokes
        # 'countsum': countsum
        # 'poker_list': poker_list
        # 'current_user': current_user
    }
    return render(request, 'dashboard.html', context)
