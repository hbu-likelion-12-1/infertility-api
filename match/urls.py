from django.urls import path
from .api import *


urlpatterns = [
    path("", MatchAPI.as_view()),
    path("code", InviteCodeAPI.as_view()),
]
