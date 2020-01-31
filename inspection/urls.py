from django.conf.urls import url
from .views import home, login, register


urlpatterns = [
    url('home', home, name='home'),
    url('login', login, name='login'),
    url('register', register, name='register')
]