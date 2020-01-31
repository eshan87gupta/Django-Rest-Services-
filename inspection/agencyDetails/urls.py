from django.conf.urls import url
from ..views import AgencyDetails

urlpatterns = [
    url('details', AgencyDetails.as_view(), name="details"),
]