from rest_framework.views import APIView, Request, Response
from users.models import User
from rest_framework import status
from bloom_ai.feedback import BloomFeedbackProvider
from question.serializers import (
    QuestionSerializer,
    QuestionAnswerSerializer,
    QuestionCommentSerializer,
)
from question.handler import QuestionHandler, MindHandler
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from app.error import AppError
from app.s3 import S3FileUploadSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from question.models import Question


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


class MindReadByQuestionAPI(APIView):
    @swagger_auto_schema(
        operation_summary="질문 ID로 마음 조회 API",
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_QUERY,
                description="질문 id",
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def get(self, req: Request, question_id: int):
        question = QuestionHandler.get_by_id(question_id)
        mind = MindHandler.find_by_question(question)
        mind["husband"] = QuestionAnswerSerializer.Model(mind["husband"])
        mind["wife"] = QuestionAnswerSerializer.Model(mind["wife"])

        return Response(data=mind, status=200)


class UploadVoiceAPI(APIView):
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(
        operation_summary="음성 데이터 업로드 API",
        manual_parameters=[
            openapi.Parameter(
                name="voice",
                in_=openapi.IN_FORM,
                type=openapi.TYPE_FILE,
                required=True,
                description="음성 데이터 파일",
            )
        ],
    )
    def post(self, req: Request, question_id: int):
        voice = req.FILES["voice"]
        if not voice:
            raise AppError(400, "음성 파일이 존재하지 않습니다")
        question = QuestionHandler.get_by_id(question_id)
        file_uploader = S3FileUploadSerializer(data={"file": voice})
        file_uploader.is_valid(raise_exception=True)
        file_url = file_uploader.save()
        updated_question = QuestionHandler.update_voice(
            question, req.user, file_url)
        data = QuestionSerializer.Model(updated_question).data
        return Response(data=data, status=201)


class CommentAPI(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="마음 댓글 작성 API",
        request_body=QuestionCommentSerializer,
    )
    def post(self, req: Request, question_id: int):
        question = get_object_or_404(Question, id=question_id)
        serializer = QuestionCommentSerializer(data=req.data)
        if serializer.is_valid():
            comment = serializer.save(writer=req.user, question=question)
            return Response(
                QuestionCommentSerializer(
                    comment).data, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
