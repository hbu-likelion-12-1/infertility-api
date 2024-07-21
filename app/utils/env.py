import os
from typing import Dict
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_PATH = os.path.join(BASE_DIR, ".env")
print(f'ENV_PATH: {ENV_PATH}')
environ.Env.read_env(ENV_PATH)

gpt_key: str = os.environ.get("GPT_KEY")
secret_key: str = os.environ.get("SECRET_KEY")
kakao_rest_api_key: str = os.environ.get("KAKAO_REST_KEY")
app_env: str = os.environ.get("ENV")

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


def get_redirect_uri():
    env = app_env
    if env == "dev":
        return "http://localhost:3000/kakao"
    return "http://galaxy4276.asuscomm.com:3000/kakao"


kakao_auth_url = "https://kauth.kakao.com/oauth/authorize"
rest_key = kakao_rest_api_key
kakao_get_code_url = f"{kakao_auth_url}?client_id={rest_key}&redirect_uri={get_redirect_uri()}&response_type=code"


class AppEnvironment:
    kakao_auth_url = kakao_get_code_url

    @staticmethod
    def gpt_key():
        if not gpt_key:
            raise EnvironmentError("GPT_KEY environment variable not set")
        return gpt_key
    
    @staticmethod
    def secret_key():
        if not secret_key:
            raise EnvironmentError("SECRET_KEY environment variable not set")
        return secret_key


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

    @staticmethod
    def run_env():
        if not app_env:
            raise EnvironmentError("ENV environment variable not set")
        return app_env
