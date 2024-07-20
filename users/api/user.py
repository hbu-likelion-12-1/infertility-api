from rest_framework.views import APIView, Request, Response
from drf_yasg.utils import swagger_auto_schema
from app.error import AppError
from users.serializers import UserSerializer


class UserCrudAPI(APIView):
    @swagger_auto_schema(operation_summary="사용자 정보 API")
    def get(self, req: Request):
        if not req.user:
            raise AppError(404, "사용자를 찾을 수 없습니다")
        user = UserSerializer.User.Model(req.user).data
        return Response(data=user, status=200)
