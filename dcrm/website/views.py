from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['UserName']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    return render(request, 'home.html',{})

def login_user(request):
    pass


def logout_user(request):
    pass



