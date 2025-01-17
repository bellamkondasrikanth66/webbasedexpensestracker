from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Function to Handle User Registration
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome aboard {username}, your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'users/register.html', {'form':form})


# Function to Handle Logout Functionality
@login_required
def logout_view(request):
    logout(request)
  
    return render(request, 'users/logout.html')