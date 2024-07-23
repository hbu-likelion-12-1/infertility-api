from django.db import models

# Create your models here.


class user_inferilities(models.Model):
    id = models.IntegerField(primary_key=True)
    # period = models.


class invite_codes(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField()
    created_at = models.DateTimeField()
    creator = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField()
    sex = models.IntegerField()

    birthday = models.CharField(max_length=10)
    created_at = models.DateTimeField()
