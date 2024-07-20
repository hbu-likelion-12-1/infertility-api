from rest_framework.views import APIView, Response, Request
from match.serializers import MatchSerializers
from app.error import AppError
from users.models import User
from match.handler import InviteCodeHandler, MatchHandler
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class MatchAPI(APIView):
    @swagger_auto_schema(operation_summary="매치 찾기 API")
    def get(self, req: Request):
        match = MatchHandler.get_by_user(req.user)
        if not match:
            return Response({"match": None}, status=200)
        return Response(data={"match": match}, status=200)

    @swagger_auto_schema(
        operation_summary="매치 체결 API",
        manual_parameters=[
            openapi.Parameter(
                "code",
                openapi.IN_QUERY,
                description="카카오 인증코드",
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def post(self, req: Request):
        query: str = req.GET.get("invite_code")
        if not query:
            raise AppError(400, "초대 코드가 존재하지 않습니다")

        invite_code = InviteCodeHandler.find_by_code(code=query)
        creator: User = invite_code.creator

        if req.user.id == creator.id:
            raise AppError(400, "초대자와 요청자가 같습니다")

        if MatchHandler.exists(creator, req.user):
            raise AppError(409, "이미 매칭된 사용자입니다")

        match = MatchHandler.create(creator, req.user)
        serialized_match = MatchSerializers.Model(match).data
        return Response(data={"match": serialized_match}, status=201)
