from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from demo.models import UserDetails


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

    user_obj = UserDetails.objects.filter(user=request.user)

    return render(request , 'Dashboard.html' , {'user_obj' : user_obj})

def admin_dashboard(request):

    user_obj = User.objects.all().exclude(is_superuser=True)
    user_list = []
    for user in user_obj:
        print(user.username)
        user_details_obj = UserDetails.objects.filter(user=user).first()
        print(user_details_obj.consumer_no)
        user_list.append(user_details_obj)
    print(user_list)


    return render(request, 'Admin_Dashboard.html' , {'user_obj' : user_list})

def admin_login(request):
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        u = authenticate(username=username, password=password)
        if u and u.is_superuser:
            login(request, u)
            print('suceess')
            return redirect('/admin_dashboard')
        else:
            pass

    return render(request, 'Admin_Login.html', {})


def logout_fn(request):
    logout(request)
    return redirect('/login')


def user_with_id(request , id):

    user_obj = UserDetails.objects.filter(consumer_no=id)

    return  render(request , 'Dashboard.html' , {'user_obj' : user_obj})