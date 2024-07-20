from django.db import models
from users.models import User


class InviteCode(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(db_comment="초대 코드")
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(
        User, related_name="creator", on_delete=models.SET_NULL, db_comment="생성한 유저"
    )


class Match(models.Model):
    id = models.IntegerField(primary_key=True)
    female = models.ForeignKey(
        User, related_name="female", on_delete=models.SET_NULL, db_comment="아내"
    )
    male = models.ForeignKey(
        User, related_name="male", on_delete=models.SET_NULL, db_comment="남편"
    )
    created_at = models.DateTimeField(auto_now_add=True, db_comment="매칭 체결일")
