from django.conf.urls import url
from ..views import MidDay

urlpatterns = [
    url('details', MidDay.as_view(), name="details"),
]