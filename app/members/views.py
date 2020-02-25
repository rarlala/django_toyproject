from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('members:user-setting')
    else:
        return redirect('members:login')


def user_setting_view(request):
    return render(request, 'members/user_setting.html')


def logout_view(request):
    logout(request)
