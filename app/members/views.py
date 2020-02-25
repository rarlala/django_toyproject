from django.shortcuts import render


def login_view(request):
    return render(request, 'members/login.html')


def user_setting_view(request):
    return render(request, 'members/user_setting.html')
