from django.db import models
from question.models import Question
from users.models import User

class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=200, db_comment="사용자 답변 내용")
    question = models.ForeignKey(
        Question, related_name="answers", on_delete=models.CASCADE, db_comment="질문"
    )
    user = models.ForeignKey(
        User, related_name="answers", on_delete=models.CASCADE, db_comment="답변 작성자"
    )
    created_at = models.DateTimeField(auto_now_add=True, db_comment="답변 작성일")  