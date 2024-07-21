from rest_framework import serializers
from match.models import Match


class MatchSerializers:
    class Model(serializers.ModelSerializer):
        class Meta:
            model = Match
            fields = '__all__'


