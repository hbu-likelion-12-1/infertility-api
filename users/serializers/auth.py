from rest_framework import serializers


class AuthSerializer:
    class Signup(serializers.Serializer):
        username = serializers.CharField(max_length=10, required=True)
        sex = serializers.CharField(max_length=1, required=True)
        birthday = serializers.DateField(required=True)
        region = serializers.CharField(max_length=20)
        city = serializers.CharField(max_length=20)
        town = serializers.CharField(max_length=20)
        care_status = serializers.CharField(max_length=30)
        cause = serializers.CharField(max_length=30)
        cost = serializers.CharField(max_length=30)
        workplace_comprehension = serializers.CharField(max_length=30)
        communication = serializers.CharField(max_length=30)
        depression_test = serializers.JSONField()
        token = serializers.CharField()

        def create(self, validated_data):
            pass

    class Login:
        pass
