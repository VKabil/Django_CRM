from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
        if request.method == 'POST':
              username = request.POST['username']
              password = request.POST['password']
              user = authenticate(request, username=username, password=password)
              if user is not None:
                    login(request, user)
                    messages.success(request, "You have been successfully Logged in......")
                    return redirect('home')
              else:
                    messages.success(request, "Your username or password incorrect, Please check the field")
                    return redirect('home')
        else:      
            return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.....")
    return redirect('home')


