from django.urls import path
from lms.views import index

urlpatterns = [path("", index, name="index")]

app_name = "lms"
