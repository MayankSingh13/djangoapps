from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "authenticator/index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("authenticator:dashboard"))
        else:
            return render(request, "authenticator/login.html", {
                'message': 'Invalid Credentials.'
            })
    else:
        return render(request, "authenticator/login.html")

def register_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = form.save()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
            messages.success(request, 'Registered successfully. Please go to login page.')
            return HttpResponseRedirect(reverse("authenticator:register"))
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, "authenticator/register.html", {
        'form':form
    })

def dashboard_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("authenticator:login"))
    return render(request, "authenticator/dashboard.html")

def logout_view(request):
    #logout the user.
    logout(request)
    return render(request, "authenticator/logout.html")
