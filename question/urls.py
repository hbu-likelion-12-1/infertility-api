from django.urls import path
from .api import *


urlpatterns = [
    path("<str:match_id>", QuestionAPI.as_view()),
]
