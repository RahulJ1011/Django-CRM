from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['UserName']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in!")
            return redirect('home')
        else:
            messages.error(request,"Invalid username or password")
    return render(request, 'home.html',{})

def login_user(request):
    
    pass


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out ........")
    return redirect('home')



