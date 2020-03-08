from django.contrib import messages
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
            messages.add_message(request, messages.ERROR, '가입되지 않은 정보입니다. 다시 확인 후 입력해주세요.')
            return render(request, 'members/login.html')

    else:
        return render(request, 'members/login.html')


def user_setting_view(request):
    if str(request.user) != 'AnonymousUser':
        return render(request, 'members/user_setting.html')
    return redirect('members:login')


def logout_view(request):
    logout(request)
    return redirect('members:login')


# 수신 상태 변경
def send_email(request):
    email = request.user
    user = User.objects.get(email=email)
    user.send_email = False if user.send_email == True else True
    user.save()
    return redirect('members:user-setting')


# 회원탈퇴 처리
def withdrawal(request):
    print('회원탈퇴 함수 접근')
    request.user.delete()
    messages.add_message(request, messages.ERROR, '회원탈퇴가 완료되었습니다.')
    return redirect('index')
