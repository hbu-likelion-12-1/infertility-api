from rest_framework.views import APIView, Request, Response
from users.models import User
from match.handler import MatchHandler
from question.handler import QuestionHandler
from question.models import Question
from bloom_ai.models import BloomFeedback
from bloom_ai.serializers import BloomSerializers
from drf_yasg.utils import swagger_auto_schema


class BloomAPI(APIView):
    @swagger_auto_schema(
        operation_summary="Bloom 리포트 API", responses={"201": BloomSerializers.Report()}
    )
    def get(self, req: Request):
        user: User = req.user
        match = MatchHandler.find_by_user(user)

        question = Question.objects.filter(
            match=match).order_by("-created_at").first()
        emotions = QuestionHandler.get_last_week_emotions(match)
        feedback = BloomFeedback.objects.filter(question=question).first()

        bloom_ai_details = BloomSerializers.Report(
            feedback, emotions=emotions).data
        return Response(data=bloom_ai_details, status=200)
