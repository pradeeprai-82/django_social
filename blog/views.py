import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Blogpost, Contact, User
from django.contrib import messages 
from django.contrib.auth  import authenticate, logout
from django.contrib.auth.models import User, auth
# Create your views here.

def index(request):
    if request.user.is_authenticated:
            post = Blogpost.objects.filter(user=request.user)
            return render(request, 'blog/index.html', {"posts": post})
    else:    
        return render(request, "blog/base.html")
    
def post(request, id):
    if request.user.is_authenticated:
        all_post = Blogpost.objects.filter(user=request.user)
        if id > len(all_post):
            return HttpResponse("Post not available")
        else:
            post = Blogpost.objects.filter(user=request.user)
            print(post)
            return render(request, "blog/post-detail.html", {"post":post})
    else:
        return render(request, "blog/base.html")

    
def contact(request):
    if request.method=="POST":
        name = request.POST('name')
        email = request.POST('email')
        phone = request.POST('phone')
        content = request.POST('content')
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
    return render(request, "blog/contact.html")

def SignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('blog/login.html')
        
        # Create the user
        user = User.objects.create_user(username, email, fname, lname, pass1)
        user.save()
        messages.success(request, " Your user has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")
    
def login(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully Logged In")
                
            post = Blogpost.objects.filter(user=request.user)            #return redirect('home', {"posts": post})
            return redirect('home')
        
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return render(request, "blog/login.html")
    else:
        
        return render(request, 'blog/login.html')
    
def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('index')

