from rest_framework import serializers
from users.models import User


class UserDetails:
    class Model(serializers.ModelSerializer):
        class Meta:
            model = User

    @staticmethod
    def exists_kakao(kakao_id: str):
        return User.objects.filter(kakao_id=kakao_id).exists()
