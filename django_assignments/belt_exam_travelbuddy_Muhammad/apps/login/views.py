from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import bcrypt

def main(request):
    return render(request, "register.html")
    
def newuser(request):
    if (request.method == "POST"):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password =  request.POST['password']
        passwordconf =  request.POST['passwordconf']
        errors = Users.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/main')
        elif password == passwordconf:
            hash1 = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            bcrypt.checkpw('password'.encode(), hash1)
            user = Users.objects.create(first_name=first_name, last_name=last_name, email=email, password=hash1)    
            user.save()
            request.session['user'] = user.id
            return redirect("/success/"+str(user.id))
        else:
            return redirect('/main')
    else:
        return redirect('main')
        
def success(request, id):
    user = Users.objects.get(id=id)
    return render(request, "success.html", {'user': user})

def login(request):
    if (request.method == "POST"):
        errors = Users.objects.login_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/main')
        # try:
        user = Users.objects.get(email= request.POST['email'])
        if (bcrypt.checkpw(request.POST['password'].encode('utf8'), user.password.encode('utf8'))):
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['email'] = user.email
            request.session['id'] = user.id
            return redirect("/travels")
        # except:
        #     return redirect("/main")
    return redirect("/main")

def logout(request):
    request.session.clear()
    return redirect("/main")

def travels(request):
    user = Users.objects.get(id=request.session['id'])
    my_trips = Trips.objects.filter(planned_by=user)
    other_trips = Trips.objects.exclude(planned_by=user)
    context = {
        'user': user,
        'my_trips': my_trips,
        'other_trips': other_trips
    }
    return render(request, "travels.html", context)

def add_trip(request):
    return render(request, "add_trip.html")

def process_trip(request):
    if (request.method == "POST"):
        errors = Trips.objects.trip_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('travel')
        else:
            errors = Trips.objects.trip_validator(request.POST)
            user = Users.objects.get(id = request.session['id'])
            trip = Trips.objects.create(location = request.POST['location'], description = request.POST['description'], travel_date_from= request.POST['travel_date_from'], travel_date_to=request.POST['travel_date_to'], user_created=user)
            trip.planned_by.add(user)
            trip.save()
            return redirect("/travels")

    # location = request.POST['location']
    # description = request.POST['description']
    # travel_date_from = request.POST['travel_date_from']
    # travel_date_to = request.POST['travel_date_to']
    return redirect("/travels")

def destination(request, id):
    trips = Trips.objects.get(id=id)
    context = {
        'trips': trips
    }
    return render(request, "destination.html", context)


def join(request, id):
    trip = Trips.objects.get(id=id)
    user = Users.objects.get(id = request.session['id'])
    trip.planned_by.add(user)
    trip.save()
    return redirect("/travels")




