from rest_framework import serializers
from question.models import Question, QuestionAnswer


class QuestionSerializer:
    class Model(serializers.ModelSerializer):
        class Meta:
            model = Question
            fields = "__all__"

    class CreateMindAnswer(serializers.Serializer):
        content = serializers.CharField(max_length=200)
        emotion = serializers.CharField(max_length=10)

    class AssembleCreateMindAnswer(serializers.Serializer):
        writer = serializers.SerializerMethodField()
        question = serializers.SerializerMethodField()
        content = serializers.SerializerMethodField()
        emotion = serializers.SerializerMethodField()

        def __init__(self, *args, **kwargs):
            self.writer = kwargs.pop("writer", None)
            self.question = kwargs.pop("question", None)
            self.content = kwargs.pop("content", None)
            self.emotion = kwargs.pop("emotion", None)
            super().__init__(*args, **kwargs)

        def save(self):
            question_answer = QuestionAnswer(
                content=self.content,
                emotion=self.emotion,
                writer=self.writer,
                question=self.question,
            )
            question_answer.save()
            return question_answer


class QuestionAnswerSerializer:
    class Model(serializers.ModelSerializer):
        class Meta:
            model = QuestionAnswer
            fields = "__all__"
