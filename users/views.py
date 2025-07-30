
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print("POST data:", request.POST)  # debug print
        if form.is_valid():
            print("Form is valid")
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        else:
            print("Form errors:", form.errors)  # debug print
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard_view(request):
    if request.user.role == 'employer':
        return render(request, 'users/employer_dashboard.html')
    else:
        return render(request, 'users/applicant_dashboard.html')

from django.shortcuts import redirect

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        return redirect('login')
    
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
