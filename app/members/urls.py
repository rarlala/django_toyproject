from django.urls import path

from members.views import login_view, user_setting_view, logout_view

app_name = 'members'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('login-out/', logout_view, name='login-out'),
    path('user-setting/', user_setting_view, name='user-setting'),
]
