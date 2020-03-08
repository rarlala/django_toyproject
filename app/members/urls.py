from django.conf.urls import url
from django.urls import path, include

from members.views import login_view, user_setting_view, logout_view, send_email

app_name = 'members'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user-setting/', user_setting_view, name='user-setting'),
    path('send-email/', send_email, name='send-email'),

    url(r'^django_popup_view_field/',
        include('django_popup_view_field.urls', namespace="django_popup_view_field")
        ),
]
