from django.db import models
from question.models import Question


class BloomFeedback(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=500, db_comment="피드백 내용")
    question = models.ForeignKey(
        Question, related_name="question_id", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, db_comment="피드백 생성일")
