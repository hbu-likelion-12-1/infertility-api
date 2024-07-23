from question.models import Question
from app.error import AppError


class QuestionHandler:
    @staticmethod
    def find_by_id(id):
        return Question.objects.get(id=id)

    @staticmethod
    def get_by_id(id):
        try:
            question = Question.objects.get(id=id)
            return question
        except Question.DoesNotExist:
            raise AppError(code=404, detail="질문이 존재하지 않습니다")
