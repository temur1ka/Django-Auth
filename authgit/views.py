from django.shortcuts import render, redirect
from .forms import regauth
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


@login_required(login_url='register')
def home(request):

    return render(request, 'home.html')

def register(request):
    form = regauth
    
    if request.method == 'POST':
        form = regauth(request.POST)
        if form.is_valid():
            form.save()
            
        messages.success(request, 'You Successfuly Created An Account')
        return redirect('login')
    context = {'form': form}

    return render(request, 'register.html', context)

def loginauth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
    
        else:        
            messages.info(request, "Username or Password is Incorrect")
        
    return render(request, 'login.html')

def logoutauth(request):
    logout(request)
    return redirect('login')