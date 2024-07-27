from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler


class AppError(APIException):
    def __init__(self, code, detail):
        self.status_code = code
        self.detail = detail
        super().__init__(detail, code)


def handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        print(f"error: {response.data}")
        custom_response_data = {
            "error": response.data.get("detail", "An error occurred")
        }
        response.data = custom_response_data

    return response
