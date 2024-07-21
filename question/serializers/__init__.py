from rest_framework import serializers
from question.models import Question


class QuestionSerializer:
    class Model(serializers.ModelSerializer):
        class Meta:
            model = Question
            fields = "__all__"
