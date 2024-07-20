from rest_framework.views import APIView, Request, Response
from drf_yasg.utils import swagger_auto_schema
from ..serializers import UserSerializer


# 회원가입 API
class SignupAPI(APIView):
    @swagger_auto_schema(
        operation_summary="회원가입 API", request_body=UserSerializer.Auth.Signup()
    )
    def post(self, req: Request):
        body = UserSerializer.Auth.Signup(data=req.data).valid()
        print(f"body: {body}")
        return Response()
