from django.db import models
from question.models import Question


class BloomFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000, db_comment="피드백 내용")
    question = models.ForeignKey(
        Question, related_name="bloom_feedbacks", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True, db_comment="피드백 생성일")
