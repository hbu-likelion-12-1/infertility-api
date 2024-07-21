from django.db import models
from match.models import Match
from users.models import User
from app.orm import TextEnumField
from app.enum import Emotion


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=500, db_comment="질문 내용")
    female_audio_url = models.URLField(db_comment="아내 음성 데이터 URL", null=True)
    male_audio_url = models.URLField(db_comment="남편 음성 데이터 URL", null=True)
    match = models.ForeignKey(
        Match, related_name="questions", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_comment="매칭 체결일")

    @staticmethod
    def create(content: str, match: Match):
        question = Question(
            content=content, match=match, female_audio_url=None, male_audio_url=None
        )
        question.save()
        return question


class QuestionAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=500, db_comment="마음 게시글 본문")
    emotion = TextEnumField(enum=Emotion)
    writer = models.ForeignKey(
        User, related_name="user_question_answers", on_delete=models.SET_NULL, null=True
    )
    question = models.ForeignKey(
        Question, related_name="question_answers", on_delete=models.CASCADE
    )
