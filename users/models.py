from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    Group,
    Permission,
)
from app.orm import TextEnumField
from app.enum import *


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "username"

    id = models.AutoField(primary_key=True)
    kakao_id = models.CharField(max_length=50)
    username = models.CharField(max_length=10)
    sex = models.CharField(max_length=1)
    region = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(Group, related_name="custom_user_groups")
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_permissions"
    )

    REQUIRED_FIELDS = ["kakao_id", "sex", "region", "city", "town", "birthday"]

    def __str__(self):
        return self.username


class UserDepressionTest(models.Model):
    id = models.IntegerField(primary_key=True)
    json = models.JSONField()
    user = models.OneToOneField(
        User, related_name="user_depression_test", on_delete=models.CASCADE
    )


class UserInfertility(models.Model):
    id = models.IntegerField(primary_key=True)
    period = TextEnumField(enum=InferPeriod)
    care_status = TextEnumField(enum=InferCareStatus)
    cause = TextEnumField(enum=InferCause)
    cost = TextEnumField(enum=InferCost)
    workplace_comprehension = TextEnumField(enum=WorkplaceComprehension)
    communication = TextEnumField(enum=InferCommunication)
    user = models.OneToOneField(
        User, related_name="user_infertility", on_delete=models.CASCADE
    )
