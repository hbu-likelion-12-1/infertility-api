from rest_framework import serializers
from botocore.config import Config
from app.utils import AppEnvironment
import boto3

s3_details = AppEnvironment.s3_details()
config = Config(signature_version="v4")
s3 = boto3.client(
    "s3",
    config=config,
    aws_access_key_id=s3_details["access_key"],
    aws_secret_access_key=s3_details["secret_key"],
    region_name=s3_details["region"],
)


class S3FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def create(self, validated_data):
        file = validated_data.get("file")
        filename = file.name

        s3.upload_fileobj(file, s3_details["bucket_name"], filename)
        return f"{s3_details['cloudfront_url']}/{filename}"
