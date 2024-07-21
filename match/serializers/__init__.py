from rest_framework import serializers
from match.models import Match
from question.serializers import QuestionSerializer


class Model(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"


class MatchSerializers:
    class Model(Model):
        pass

    class WithQuestion(serializers.ModelSerializer):
        match = Model()
        question = QuestionSerializer.Model()

        class Meta:
            model = Match
            fields = ["match", "question"]

        def to_representation(self, instance):
            return {
                "match": Model(instance["match"]).data,
                "question": QuestionSerializer.Model(instance["question"]).data,
            }
