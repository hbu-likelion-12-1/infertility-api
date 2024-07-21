from django.urls import path
from .api import *


urlpatterns = [
    path("<int:match_id>", QuestionAPI.as_view()),
]
