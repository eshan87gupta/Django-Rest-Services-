from django.conf.urls import url
from ..views import Teacher

urlpatterns = [
    url('teachers', Teacher.as_view(), name="teachers"),
]