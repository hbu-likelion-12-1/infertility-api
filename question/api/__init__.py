from rest_framework.views import APIView, Request, Response
from app.error import AppError
from match.handler import MatchHandler
from question.provider import QuestionProvider
from drf_yasg.utils import swagger_auto_schema
from question.serializers import QuestionSerializer, QuestionAnswerSerializer
from .mind import MindAnswerAPI, MindReadAPI, UploadVoiceAPI, MindReadByQuestionAPI


class QuestionAPI(APIView):
    @swagger_auto_schema(operation_summary="새로운 질문 생성 API")
    def post(self, req: Request, match_id: int):
        match = MatchHandler.find_by_id(match_id)
        question_provider = QuestionProvider(match=match)
        question = question_provider.create_question()
        json = QuestionSerializer.Model(question).data
        return Response(data={"question": json}, status=200)
