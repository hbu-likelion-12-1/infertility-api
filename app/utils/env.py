import os
from typing import Dict
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

gpt_key: str = os.environ.get("GPT_KEY")
kakao_rest_api_key: str = os.environ.get("KAKAO_REST_KEY")

database_details: Dict[str, str] = {
    "name": os.environ.get("DB_NAME"),
    "ip": os.environ.get("DB_IP"),
    "port": os.environ.get("DB_PORT"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
}


def check_none_in_dict(d: dict) -> bool:
    for key, value in d.items():
        if value is None:
            print(f"Environment variable for {key} is not set.")
            return True
    return False


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

    @staticmethod
    def database_details():
        if check_none_in_dict(database_details):
            raise EnvironmentError("DATABASE environment variable not set")
        return database_details
