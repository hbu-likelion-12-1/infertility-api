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
    id = models.AutoField(primary_key=True)
    kakao_id = models.CharField(max_length=50)
    username = models.CharField(max_length=10)
    sex = models.CharField(max_length=1)
    region = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    depression_test = models.OneToOneField(
        "UserDepressionTest",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user",
    )
    infertility = models.OneToOneField(
        "UserInfertility",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="user",
    )

    groups = models.ManyToManyField(Group, related_name="custom_user_groups")
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_permissions"
    )

    USERNAME_FIELD = "id"
    REQUIRED_FIELDS = ["kakao_id", "sex", "region", "city", "town", "birthday"]

    def __str__(self):
        return self.username

    @staticmethod
    def create(data):
        user: User = User(
            username=data["username"],
            sex=data["sex"],
            region=data["region"],
            city=data["city"],
            town=data["town"],
            birthday=data["birthday"],
            kakao_id=data["kakao_id"],
        ).save()

        depression_test = UserDepressionTest(
            json=data["depression_test"], user=user
        ).save()

        user_infer = UserInfertility(
            period=data["period"],
            care_status=data["care_status"],
            cause=data["cause"],
            cost=data["cost"],
            workplace_comprehension=data["workplace_comprehension"],
            communication=data["communication"],
            user=user,
        ).save()

        user.infertility = user_infer
        user.depression_test = depression_test
        user.save()

        return user


class UserDepressionTest(models.Model):
    id = models.IntegerField(primary_key=True)
    json = models.JSONField()


class UserInfertility(models.Model):
    id = models.IntegerField(primary_key=True)
    period = TextEnumField(enum=InferPeriod)
    care_status = TextEnumField(enum=InferCareStatus)
    cause = TextEnumField(enum=InferCause)
    cost = TextEnumField(enum=InferCost)
    workplace_comprehension = TextEnumField(enum=WorkplaceComprehension)
    communication = TextEnumField(enum=InferCommunication)


class OAuthIdentifier(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.CharField()
