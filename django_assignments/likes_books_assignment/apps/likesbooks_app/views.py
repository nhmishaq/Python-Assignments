from django.shortcuts import render, HttpResponse, redirect
from models import Users, Books
from django.core.exceptions import ObjectDoesNotExist
import bcrypt


def index(request):
    context = {

    }
    return render (request, "index.html", context)