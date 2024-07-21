from django.test import TestCase
from .gpt import gpt_client
from .question import BloomQuestionCreator


class SimpleGptTest(TestCase):
    def test_gpt_simple_request(self):
        creator = BloomQuestionCreator(None, None)

        completion = gpt_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": creator.question_creator_template}],
        )
        print(completion)
