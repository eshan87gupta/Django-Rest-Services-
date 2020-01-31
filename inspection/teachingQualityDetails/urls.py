from django.conf.urls import url
from ..views import Teaching

urlpatterns = [
    url('quality', Teaching.as_view(), name="quality"),
]