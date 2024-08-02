from rest_framework import serializers
from users.models import User
from question.handler import MindHandler


class UserDetails:
    class Model(serializers.ModelSerializer):
        class Meta:
            model = User

            exclude = [
                "last_login",
                "is_superuser",
                "kakao_id",
                "groups",
                "user_permissions",
            ]

    @staticmethod
    def exists_kakao(kakao_id: str):
        return User.objects.filter(kakao_id=kakao_id).exists()

    class UserWithQuestionId(serializers.ModelSerializer):
        mind_id = serializers.SerializerMethodField()

        class Meta:
            model = User
            exclude = [
                "last_login",
                "is_superuser",
                "kakao_id",
                "groups",
                "user_permissions",
                "depression_test",
                "infertility",
                "region",
                "city",
                "town",
                "birthday",
                "created_at",
                "password",
            ]

        def get_mind_id(self, obj: User):
            mind = MindHandler.first_by_user(user=obj)
            if not mind:
                self.mind_id = None
                return
            self.mind_id = mind.id
            return mind.id
