from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from members.models import User


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    if request.method == 'POST':
        email = request.POST['username']
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.add_message(request, messages.ERROR, '앗! 이미 사용중인 email입니다.')
            return redirect('index')

        user = User.objects.create_user(
            password=password,
            username=username,
            email=email,
            send_email=True
        )

        if user is not None:
            login(request, user)
            return redirect('members:user-setting')

        return redirect('members:login')
