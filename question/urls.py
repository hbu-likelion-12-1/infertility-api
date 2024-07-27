from django.urls import path
from . import views
from .api import *


urlpatterns = [
    path("<str:match_id>/", QuestionAPI.as_view()),
    path("mind/answer/<int:question_id>/", MindAnswerAPI.as_view()),
    path("mind/<int:mind_id>", MindReadAPI.as_view()),
    path("mind/voice/<int:question_id>/", UploadVoiceAPI.as_view()),
    path("questions/<int:question_id/", views.question_detail, name="question_detail"),
]
