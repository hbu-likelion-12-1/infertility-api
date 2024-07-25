from rest_framework.views import APIView, Response, Request
from question.models import Question
from question.serializers import QuestionSerializer
from match.handler import MatchHandler
from drf_yasg.utils import swagger_auto_schema


class StorageListAPI(APIView):
    @swagger_auto_schema(operation_summary="보관함 조회 API")
    def get(self, req: Request):
        match = MatchHandler.find_by_user(user=req.user)
        questions = list(Question.objects.filter(match=match))
        data = QuestionSerializer.Model(questions, many=True).data
        return Response(data=data, status=200)
