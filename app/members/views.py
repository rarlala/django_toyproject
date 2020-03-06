from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

User = get_user_model()


def login_view(request):
    if request.method == 'POST':
        # email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('members:user-setting')
    else:
        return render(request, 'members/login.html')


def user_setting_view(request):
    return render(request, 'members/user_setting.html')


def logout_view(request):
    logout(request)
    return redirect('members:login')


# 수신 상태 변경
def send_email(request):
    email = request.user
    user = User.objects.get(email=email)
    user.send_email = False if user.send_email==True else True
    user.save()
    return redirect('members:user-setting')
