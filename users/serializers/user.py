from rest_framework import serializers
from users.models import User


class UserDetails:
    class Model(serializers.ModelSerializer):
        class Meta:
            model = User
