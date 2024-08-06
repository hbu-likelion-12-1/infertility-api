from django.urls import path
from .api import *



urlpatterns = [
    path("", BloomAPI.as_view()),
    path("recommend/", RecommendView.as_view(), name='recommend'),
]