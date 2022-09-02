from django.urls import path

from .views import home

app_name = 'accountapp'

urlpatterns = [
    path('home/', home, name='home'),
]