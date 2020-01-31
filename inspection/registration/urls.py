from django.conf.urls import url
from ..views import Registration

urlpatterns = [
    url('register', Registration.as_view(), name="register"),
]