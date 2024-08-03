from django.urls import path
from .api import *
from .api.mind import CommentAPI


urlpatterns = [
    path("<str:match_id>/", QuestionAPI.as_view()),
    path("mind/answer/<int:question_id>/", MindAnswerAPI.as_view()),
    path("mind/<int:mind_id>/", MindReadAPI.as_view()),
    path("mind/both/<int:question_id>/", MindReadByQuestionAPI.as_view()),
    path("mind/voice/<int:question_id>/", UploadVoiceAPI.as_view()),
    path(
        "mind/<int:question_id>/comments/",
        CommentAPI.as_view(),
        name="question_comment",
    ),
]
