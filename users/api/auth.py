from rest_framework.views import APIView, Request, Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from ..serializers import UserSerializer
from app.utils import AppEnvironment
from rest_framework.permissions import AllowAny
from users.kakao import KakaoProvider
from .login import LoginService


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


class KakaoLoginAPI(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="카카오 로그인 API",
        manual_parameters=[
            openapi.Parameter(
                "code",
                openapi.IN_QUERY,
                description="카카오 인증코드",
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def get(self, req: Request):
        auth_code = req.GET.get("code")
        kakao = KakaoProvider(auth_code=auth_code)
        kakao.get_token()
        kakao_user_id = kakao.login()
        login_details = LoginService.login(kakao_id=kakao_user_id)
        return Response(data=login_details, status=200)
