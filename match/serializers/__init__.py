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

    class Integrated(serializers.Serializer):
        id = serializers.SerializerMethodField()
        husband = serializers.SerializerMethodField()
        wife = serializers.SerializerMethodField()
        question = serializers.SerializerMethodField()

        def __init__(self, *args, **kwargs):
            self.match_id = kwargs.pop("match_id", None)
            self.husband_instance = kwargs.pop("husband_instance", None)
            self.wife_instance = kwargs.pop("wife_instance", None)
            self.question_instance = kwargs.pop("question_instance", None)
            super().__init__(*args, **kwargs)

        def get_id(self, obj):
            return self.match_id if self.match_id else None

        def get_husband(self, obj):
            return (
                UserDetails.UserWithQuestionId(
                    self.husband_instance, question=self.question_instance
                ).data
                if self.husband_instance
                else None
            )

        def get_wife(self, obj):
            wife = (
                UserDetails.UserWithQuestionId(
                    self.wife_instance, question=self.question_instance
                ).data
                if self.wife_instance
                else None
            )
            return wife

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
