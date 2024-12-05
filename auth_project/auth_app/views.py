from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'auth_app/home.html')

@login_required
def index(request):
    return render(request, 'auth_app/index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'auth_app/register.html', {'form': form})
