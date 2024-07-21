from rest_framework.views import APIView, Request, Response
from users.api.login import LoginService
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import AllowAny


class TestUserAPI(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="목업 유저 카카오 로그인 API",
        manual_parameters=[
            openapi.Parameter(
                "type",
                openapi.IN_QUERY,
                description="어떤 사용자로 로그인 할 지(husband 혹은 wife)",
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def get(self, req: Request):
        type = req.GET.get("type")
        kakao_id = self.get_kakao_id(type)
        user_details = LoginService.login(kakao_id)
        return Response(data=user_details, status=200)

    def get_kakao_id(self, type: str):
        if type == "husband":
            return "99999999"
        return "99999998"
