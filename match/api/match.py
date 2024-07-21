from rest_framework.views import APIView, Response, Request
from match.serializers import MatchSerializers
from app.error import AppError
from users.models import User
from match.handler import InviteCodeHandler, MatchHandler
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from question.provider import QuestionProvider


class MatchAPI(APIView):
    @swagger_auto_schema(operation_summary="매치 찾기 API")
    def get(self, req: Request):
        user = req.user

        if not user:
            return Response({"detail": "인증되지 않은 사용자입니다"}, status=401)

        match = MatchHandler.get_by_user(user)
        if not match:
            return Response({"match": None}, status=200)

        serialized_match = MatchSerializers.Model(match).data
        return Response(data={"match": serialized_match}, status=200)

    @swagger_auto_schema(
        operation_summary="매치 체결 API",
        manual_parameters=[
            openapi.Parameter(
                "code",
                openapi.IN_QUERY,
                description="매칭 코드",
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def post(self, req: Request):
        query: str = req.GET.get("code")

        if not query:
            raise AppError(400, "초대 코드가 존재하지 않습니다")

        try:
            invite_code = InviteCodeHandler.find_by_code(code=query)
        except AppError as e:
            return Response({"detail": str(e)}, status=400)

        creator: User = invite_code.creator

        validate_create_match(creator, req.user)
        match = MatchHandler.create(creator, req.user)
        first_question = QuestionProvider(match=match).create_question()

        result_serializer = MatchSerializers.WithQuestion(
            {"match": match, "question": first_question}
        )
        return Response(data=result_serializer.data, status=201)


def validate_create_match(u1: User, u2: User):
    if u1.id == u2.id:
        raise AppError(400, "초대자와 요청자가 같습니다")

    if MatchHandler.exists(u1, u2):
        raise AppError(409, "이미 매칭된 사용자입니다")
