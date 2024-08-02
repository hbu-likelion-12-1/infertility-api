from django.urls import path
from .api import *
from .views import recommend_view

urlpatterns = [
    path("", BloomAPI.as_view()),
    path('recommend/', recommend_view, name='recommend')
]
