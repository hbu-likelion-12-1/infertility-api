from rest_framework import serializers
from bloom_ai.models import BloomFeedback


class Model(serializers.ModelSerializer):
    class Meta:
        model = BloomFeedback
        fields = "__all__"


class BloomSerializers:
    class Report(serializers.ModelSerializer):
        feedback = Model()
        emotions = serializers.SerializerMethodField()

        class Meta:
            model = BloomFeedback
            fields = ["feedback", "emotions"]

        def __init__(self, *args, **kwargs):
            self.emotions = kwargs.pop("emotions", [])
            super().__init__(*args, **kwargs)
