from django.core.mail import send_mail
from django.shortcuts import render

from config.settings import EMAIL_HOST_USER
from mail import forms


def mail(request):
    sub = forms.Mail()

    if request.method == 'POST':
        sub = forms.Mail(request.POST)
        subject = '[안내] 웰킵스 구매 가능 알림'
        message = '웰킵스 마스크 구매가 가능합니다!'
        recepient = 'wtw9611@gmail.com'
        # recepient = str(sub['Email'].value)
        send_mail(subject, EMAIL_HOST_USER, message, [recepient])
        return render(request, 'mail/success.html', {'recepient': recepient})

    return render(request, 'mail/index.html', {'forms': sub})
