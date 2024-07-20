from match.models import InviteCode, Match
from app.error import AppError
from users.models import User
from django.db.models import Q


class InviteCodeHandler:
    @staticmethod
    def find_by_code(code: str):
        invite_code: InviteCode = InviteCode.objects.get(code=code)
        if not invite_code:
            raise AppError(404, "초대 코드가 존재하지 않습니다")

        return invite_code


class MatchHandler:
    @staticmethod
    def exists(u1: User, u2: User):
        return Match.objects.exists(
            (Q(female=u1) or Q(female=u2)) or (Q(male=u1) or Q(male=u2))
        )

    @staticmethod
    def create(u1: User, u2: User):
        return Match.create(u1, u2)

    @staticmethod
    def get_by_user(user: User):
        return Match.objects.get(Q(female=user) or Q(male=user))
