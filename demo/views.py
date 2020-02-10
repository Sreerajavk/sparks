from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request):

    return  render(request , 'Home.html')

@csrf_exempt
def login_fn(request):

    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        u = authenticate(username=username, password=password)
        if u:
            login(request,u)
            print('suceess')
            return redirect('/dashboard')
        else:
            pass

    return  render(request , 'Login.html' , {})


def index(request):
    return redirect('/home')


def dashboard(request):
    return render(request , 'Dashboard.html')