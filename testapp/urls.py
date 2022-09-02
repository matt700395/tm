from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from testapp.views import hello_world

app_name = "testapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
]