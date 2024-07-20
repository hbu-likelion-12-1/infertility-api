from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User
from users.serializers import UserSerializer


class LoginService:
    @staticmethod
    def login(kakao_id: str):
        user: User = User.objects.filter(kakao_id=kakao_id).get()
        if not user:
            return {"user": None, "access_token": None, "kakao_id": kakao_id}

        refresh = RefreshToken.for_user(user)
        user_details = UserSerializer.User.Model(user).data
        access_token = str(refresh.access_token)

        return {
            "user": user_details,
            "access_token": access_token,
            "kakao_id": kakao_id,
        }
