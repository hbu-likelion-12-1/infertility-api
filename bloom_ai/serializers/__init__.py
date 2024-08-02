from rest_framework import serializers
from bloom_ai.models import BloomFeedback


class Model(serializers.ModelSerializer):
    class Meta:
        model = BloomFeedback
        fields = "__all__"


class BloomSerializers:
    class Report(serializers.Serializer):
        feedback = serializers.SerializerMethodField()
        emotions = serializers.SerializerMethodField()

        def __init__(self, *args, **kwargs):
            self.emotions = kwargs.pop("emotions", [])
            self.feedback_instance = kwargs.pop("feedback_instance", None)
            super().__init__(*args, **kwargs)

        def get_feedback(self, obj):
            return (
                Model(self.feedback_instance).data if self.feedback_instance else None
            )

        def get_emotions(self, obj):
            return self.emotions
