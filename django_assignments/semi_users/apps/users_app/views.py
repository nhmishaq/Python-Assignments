from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'created_at': created_at
    }
    print "MADE IT TO INDEX"
    return render (request, index.html, context)

def create_new(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    created_at = request.POST['created_at']
    User.objects.create(full_name=str(first_name) + str(last_name), email=email, created_at=created_at)
    return redirect('/')

# def show_user(request):
    
# def edit_user(request):