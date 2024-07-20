from rest_framework.views import APIView, Request, Response
from drf_yasg.utils import swagger_auto_schema
from ..serializers import UserSerializer
from app.utils import AppEnvironment
from rest_framework.permissions import AllowAny


# 회원가입 API
class SignupAPI(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="회원가입 API", request_body=UserSerializer.Auth.Signup()
    )
    def post(self, req: Request):
        signup_handler = UserSerializer.Auth.Signup(data=req.data)
        signup_handler.is_valid(raise_exception=True)

        return Response()


class KakaoRedirectAPI(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(operation_summary="카카오 인증 URL 리다이렉트 API")
    def get(self, req):
        return Response(data=AppEnvironment.kakao_auth_url, status=302)
