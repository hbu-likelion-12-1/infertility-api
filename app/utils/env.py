import os

gpt_key: str = os.getenv("GPT_KEY")
kakao_rest_api_key: str = os.getenv("KAKAO_REST_KEY")


class AppEnvironment:
    @staticmethod
    def gpt_key():
        if not gpt_key:
            raise EnvironmentError("GPT_KEY environment variable not set")
        return gpt_key

    @staticmethod
    def kakao_rest_api():
        if not kakao_rest_api_key:
            raise EnvironmentError(
                "KAKAO_REST_KEY environment variable not set")
        return kakao_rest_api_key
