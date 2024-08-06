from rest_framework.views import APIView, Request, Response
from users.models import User
from match.handler import MatchHandler
from question.handler import QuestionHandler
from question.models import Question
from bloom_ai.models import BloomFeedback
from bloom_ai.serializers import BloomSerializers
from bloom_ai.recommend import BloomRecommend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



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
            instance=feedback, feedback_instance=feedback, emotions=emotions
        ).data
        return Response(data=bloom_ai_details, status=200)


class RecommendView(APIView):
    @swagger_auto_schema(
        operation_summary="추천 활동 API",
        manual_parameters=[
            openapi.Parameter('latitude', openapi.IN_QUERY, description="위도", type=openapi.TYPE_STRING),
            openapi.Parameter('longitude', openapi.IN_QUERY, description="경도", type=openapi.TYPE_STRING)
        ],
        responses={200: 'OK', 400: 'Bad Request'}
    )
    def get(self, req: Request):
        latitude = req.GET.get("latitude")
        longitude = req.GET.get("longitude")

        if not latitude or not longitude:
            return Response({"error": "위도와 경도를 제공해주세요."}, status=status.HTTP_400_BAD_REQUEST)

        bloom_recommend = BloomRecommend()
        recommendations = bloom_recommend.recommend_activity(latitude, longitude)

        return Response({"recommendations": recommendations}, status=status.HTTP_200_OK)
