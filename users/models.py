from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from app.orm import TextEnumField
from app.enum import *


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "username"

    id = models.IntegerField(primary_key=True)
    kakao_id = models.CharField()
    username = models.CharField(max_length=10)
    sex = models.CharField(max_length=1)
    region = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    birthday = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = [username, sex, region, city, town, birthday]


class UserDepressionTest(models.Model):
    id = models.IntegerField(primary_key=True)
    json = models.JSONField()
    user = models.OneToOneField(
        User, related_name="user_id", on_delete=models.CASCADE)


class UserInfertility(models.Model):
    id = models.IntegerField(primary_key=True)
    period = TextEnumField(enum=InferPeriod)
    care_status = TextEnumField(enum=InferCareStatus)
    cause = TextEnumField(enum=InferCause)
    cost = TextEnumField(enum=InferCost)
    workplace_comprehension = TextEnumField(enum=WorkplaceComprehension)
    communication = TextEnumField(enum=InferCommunication)
    user = models.OneToOneField(
        User, related_name="user_id", on_delete=models.CASCADE)
