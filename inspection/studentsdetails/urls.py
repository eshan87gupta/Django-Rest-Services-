from django.conf.urls import url
from ..views import StudentData

urlpatterns = [
    url('details', StudentData.as_view(), name="details"),
]