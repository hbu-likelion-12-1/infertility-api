from rest_framework.views import APIView, Request, Response
from users.models import User
from rest_framework import status
from bloom_ai.feedback import BloomFeedbackProvider
from question.serializers import QuestionSerializer, QuestionAnswerSerializer
from question.handler import QuestionHandler, MindHandler
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


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


class MindReadAPI(APIView):
    @swagger_auto_schema(
        operation_summary="마음 조회 API",
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="마음 id",
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def get(self, req: Request, mind_id: int):
        mind = MindHandler.find_by_id(mind_id)
        data = QuestionAnswerSerializer.Model(mind).data
        return Response(data=data, status=200)
