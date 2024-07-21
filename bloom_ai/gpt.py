from openai import OpenAI
from app.utils import AppEnvironment

gpt_client = OpenAI(
    api_key=AppEnvironment.gpt_key(),
)


class BloomAI:
    client = gpt_client

    def query(self, message: str) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-4o", messages=[{"role": "user", "content": message}]
        )

        return completion.choices[0].message.content
