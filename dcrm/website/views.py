from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignupForm
def home(request):
    if request.method == 'POST':
        username = request.POST.get('UserName', None)
        password = request.POST.get('password', None)
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


def register_user(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request,"You have sucessfully registered!!!!!!")
            return redirect('home')
        
    else:
        form = SignupForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})



