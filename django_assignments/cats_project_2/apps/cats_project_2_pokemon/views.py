from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    print "MADE IT TO INDEX"
    return render(request, "index.html")