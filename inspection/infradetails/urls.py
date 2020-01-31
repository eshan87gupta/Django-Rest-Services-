from django.conf.urls import url
from ..views import Infrastructure

urlpatterns = [
    url('details', Infrastructure.as_view(), name="details"),
]