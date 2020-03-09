from django.urls import path

from mail.views import mail

urlpatterns = [
    path('', mail, name='mail'),
]