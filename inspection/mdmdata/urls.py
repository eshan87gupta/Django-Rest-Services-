from django.conf.urls import url
from ..views import MDMDataBase

urlpatterns = [
    url('details/', MDMDataBase.as_view(), name="pics"),
]