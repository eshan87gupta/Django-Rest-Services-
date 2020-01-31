from django.conf.urls import url
from ..views import LoadData

urlpatterns = [
    url('data', LoadData.as_view(), name="pics"),
]