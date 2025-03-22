from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserSignupForm
from .models import FarmerProfile, CertificationRequest, User


def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')  
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def dashboard_view(request):
    if request.user.role == 'Customer':
        return redirect('customer_dashboard')
    elif request.user.role == 'Farmer':
        return redirect('farmer_dashboard')
    elif request.user.role == 'Admin':
        return redirect('admin_dashboard')
    elif request.user.role == 'Verifier':
        return redirect('verifier_dashboard')
    else:
        messages.error(request, "Invalid user role.")
        return redirect('home')  # Redirect to home if the role is invalid

def customer_dashboard(request):
    return render(request, 'customer/customer_dashboard.html')

def farmer_dashboard(request):
    return render(request, 'farmer/farmer_dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

def verifier_dashboard(request):
    return render(request, 'verifier/verifier_dashboard.html')

def index_view(request):
    return render(request, 'index.html')

