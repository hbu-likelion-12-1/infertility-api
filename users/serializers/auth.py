from rest_framework import serializers


class AuthSerializer:
    class Signup(serializers.Serializer):
        username = serializers.CharField(max_length=10, required=True)
        sex = serializers.CharField(max_length=1, required=True)
        birthday = serializers.DateField(required=True)
        region = serializers.CharField(max_length=20)
        city = serializers.CharField(max_length=20)
        town = serializers.CharField(max_length=20)

        def valid(self):
            self.is_valid(raise_exception=True)
            return self.validated_data

    class Login:
        pass
