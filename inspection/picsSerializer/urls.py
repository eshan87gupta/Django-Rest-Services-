from django.conf.urls import url
from ..views import SchoolImages

urlpatterns = [
    url('pics/', SchoolImages.as_view(), name="pics"),
]