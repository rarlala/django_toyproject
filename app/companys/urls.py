from django.urls import path

from companys.views import crawling

app_name = 'companys'

urlpatterns = [
    path('crawling/', crawling, name='crawling')
]