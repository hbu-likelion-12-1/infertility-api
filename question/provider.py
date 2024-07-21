from match.models import Match
from users.models import User
from bloom_ai.question import BloomQuestionCreator


class QuestionProvider:

    match = None

    def __init__(self, match: Match):
        self.match = match

    def create_question(self):
        husband = self.get_husband(self.match.male, self.match.female)
        wife = self.get_wife(self.match.male, self.match.female)
        question = BloomQuestionCreator(
            husband=husband, wife=wife).create(self.match)
        return question

    def get_husband(self, u1: User, u2: User):
        if u1.sex == "M":
            return u1
        return u2

    def get_wife(self, u1: User, u2: User):
        if u1.sex == "F":
            return u1
        return u2
