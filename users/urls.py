from django.urls import path
from .api import *


urlpatterns = [
    path("auth/signup/", SignupAPI.as_view()),
]
