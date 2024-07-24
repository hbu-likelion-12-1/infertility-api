from rest_framework import serializers
from match.models import Match
from question.serializers import QuestionSerializer
from users.serializers import UserDetails


class Model(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = "__all__"


class MatchSerializers:
    class Model(Model):
        pass

    class Integrated(serializers.ModelSerializer):
        match = serializers.SerializerMethodField()
        husband = serializers.SerializerMethodField()
        wife = serializers.SerializerMethodField()
        question = serializers.SerializerMethodField()

        class Meta:
            model = Match
            fields = ["match", "husband", "wife", "question"]

        def __init__(self, *args, **kwargs):
            self.match_instance = kwargs.pop("match", None)
            self.husband_instance = kwargs.pop("husband", None)
            self.wife_instance = kwargs.pop("wife", None)
            self.question_instance = kwargs.pop("question", None)
            super().__init__(*args, **kwargs)

        def get_match(self, obj):
            return self.match

        def get_husband(self, obj):
            return (
                UserDetails.UserWithQuestionId(self.husband_instance).data
                if self.husband_instance
                else None
            )

        def get_wife(self, obj):
            return (
                UserDetails.UserWithQuestionId(self.wife_instance).data
                if self.wife_instance
                else None
            )

        def get_question(self, obj):
            return (
                QuestionSerializer.Model(self.question_instance).data
                if self.question_instance
                else None
            )

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
