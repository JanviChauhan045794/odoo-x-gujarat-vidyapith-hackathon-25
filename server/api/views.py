from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignupForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def signup_view(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')  # Change 'login' to your login url name
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})




@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_success_view(request):
    return render(request, 'logout_success.html')
