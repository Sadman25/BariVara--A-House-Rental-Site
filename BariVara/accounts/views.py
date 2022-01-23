from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import userRegistration,profileRegistration
# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect ('homePage')
        else:
            messages.info (request, 'Email address or Password is incorrect')
            
    return render (request,'loginpage.html')

def registration(request):
    userForm = userRegistration()
    profileForm = profileRegistration()

    if request.method == 'POST':
        userForm = userRegistration(request.POST)
        profileForm = profileRegistration(request.POST,request.FILES)
        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            profile = profileForm.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request,'Account was created for ' + profile.user.username)
            return redirect ('loginPage')

    else:
        print(userForm.errors, profileForm.errors)
    
    context = {
        'userForm':userForm,
        'profileForm':profileForm
    }
    return render (request,'registration.html',context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')