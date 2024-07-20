from rest_framework.views import APIView, Response, Request
from match.models import InviteCode
from drf_yasg.utils import swagger_auto_schema


class InviteCodeAPI(APIView):
    @swagger_auto_schema(operation_summary="초대 코드 발급 API")
    def post(self, req: Request):
        invite_code: InviteCode = InviteCode(creator=req.user).save()
        return Response(data={"invite_code": invite_code.code}, status=201)
