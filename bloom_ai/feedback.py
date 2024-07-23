from .gpt import BloomAI
from question.models import QuestionAnswer, Question
from .models import BloomFeedback
from typing import List


def divide_answers_by_sex(answers: List[QuestionAnswer]):
    husband = None
    wife = None

    for answer in answers:
        if answer.writer.sex is "F":
            wife = answer
        if answer.writer.sex is "M":
            husband = answer

    return [husband, wife]


class BloomFeedbackProvider:
    template = """
You're a counselor who listens to fertility couples' concerns.

Based on the couple's answers to your preliminary questions, you want to understand their feelings and offer positive advice, encouragement, and recommendations for ways to improve their situation.

The format of the questions and answers will be as follows.

Question: [Question]
Husband Answer: [Answer]
Wife Answer: [Answer]

Now, here's the data I'm giving you.
Question: {question}
Husband Answer: {husband_answer}
Wife Answer: {wife_answer}
Give me the result of this in Korean
    """
    bloom_ai = BloomAI()

    def create_or_update(self, mind_answer: QuestionAnswer):
        question = mind_answer.question
        minds = list(QuestionAnswer.objects.filter(question=question))
        [husband, wife] = divide_answers_by_sex(minds)

        exists_feedback: BloomFeedback = BloomFeedback.objects.filter(
            question=mind_answer.question
        ).first()
        if exists_feedback is not None:
            return self.update(feedback=exists_feedback, husband=husband, wife=wife)
        return self.create(question, husband, wife)

    def create(self, question: Question, husband: QuestionAnswer, wife: QuestionAnswer):
        assembled = self.assemble_template(
            question.content, husband.content, wife.content
        )
        query_result = self.bloom_ai.query(assembled)
        feedback = BloomFeedback(question=question, content=query_result)
        feedback.save()
        return feedback

    def update(
        self, feedback: BloomFeedback, husband: QuestionAnswer, wife: QuestionAnswer
    ):
        assembled = self.assemble_template(
            feedback.question.content, husband.content, wife.content
        )
        query_result = self.bloom_ai.query(assembled)
        feedback.content = query_result
        feedback.save()
        return feedback

    def assemble_template(self, question: str, husband: str, wife: str):
        return self.template.format(
            question=question, husband_answer=husband, wife_answer=wife
        )
