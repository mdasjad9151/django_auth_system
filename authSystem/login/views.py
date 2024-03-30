from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    return HttpResponse("hhh")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')  # Redirect to home page after successful login
        else:
            # Handle invalid login
            pass
    return render(request, 'login/login.html')

# @login_required
# def home_view(request):
#     return render(request, 'accounts/home.html')

def logout_view(request):
    logout(request)
    return redirect('')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})