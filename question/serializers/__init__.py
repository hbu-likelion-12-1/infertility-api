from rest_framework import serializers
from question.models import Question


class QuestionSerializer:
    class Model(serializers.ModelSerializer):
        husband_mind = serializers.SerializerMethodField()
        wife_mind = serializers.SerializerMethodField()

        class Meta:
            model = Question
            fields = "__all__"
