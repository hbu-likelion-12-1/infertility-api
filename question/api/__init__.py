from rest_framework.views import APIView, Request, Response
from app.error import AppError
from match.handler import MatchHandler
from question.provider import QuestionProvider
from drf_yasg.utils import swagger_auto_schema
from question.serializers import QuestionSerializer, QuestionAnswerSerializer
from users.models import User
from question.handler import QuestionHandler
from rest_framework import status
from bloom_ai.feedback import BloomFeedbackProvider


class QuestionAPI(APIView):
    @swagger_auto_schema(operation_summary="새로운 질문 생성 API")
    def post(self, req: Request, match_id: int):
        match = MatchHandler.find_by_id(match_id)
        question_provider = QuestionProvider(match=match)
        question = question_provider.create_question()
        json = QuestionSerializer.Model(question).data
        return Response(data={"question": json}, status=200)


class MindAnswerAPI(APIView):
    feedback_provider = BloomFeedbackProvider()

    @swagger_auto_schema(
        operation_summary="질문에 대한 마음 작성 API",
        request_body=QuestionSerializer.CreateMindAnswer,
    )
    def post(self, req: Request, question_id: int):
        data = req.data
        body_serial = QuestionSerializer.CreateMindAnswer(data=data)
        body_serial.is_valid(raise_exception=True)
        body = body_serial.data

        writer: User = req.user
        question = QuestionHandler.get_by_id(question_id)
        question_serial = QuestionSerializer.AssembleCreateMindAnswer(
            writer=writer,
            question=question,
            content=body["content"],
            emotion=body["emotion"],
        )
        result = question_serial.save()
        self.feedback_provider.create_or_update(result)
        created_data = QuestionAnswerSerializer.Model(result).data

        return Response(data=created_data, status=status.HTTP_201_CREATED)
