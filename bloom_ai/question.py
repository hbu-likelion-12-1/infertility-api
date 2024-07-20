from users.models import User
from question.models import Question
from match.models import Match
from typing import List


class BloomQuestionCreator:
    question_creator_template = """
I'm developing a service that provides psychological counseling for infertile couples.
I'm thinking of questions to ask in the service to counsel infertile couples.

I need you to create one question to be delivered to infertile couples in Korean like the example below.
Note: Please answer only in the format below.

Example) Question: (Question content)

I'll provide the following data about husband and wife And below are examples of questions.
Example)
 - Timing of infertility diagnosis:
 - Situation of infertility treatment:
 - Main causes of infertility:
 - Financial burden of infertility treatment:
 - Support from family or others: - Understanding of infertility in the workplace:
 - Communication about fertility issues between the couple:

**Husband**.
 - Timing of infertility diagnosis: {male_age_of_diagnosis}
 - Situation of infertility treatment: {male_fertility_treatment_situation}
 - Main causes of infertility: {male_main_cause_of_infertility}
 - Financial burden of infertility treatment: {male_economic_burden_of_treatment}
 - Support from family or others: {male_support_from_family}
 - Understanding of infertility in the workplace: {male_understanding_in_workplace}
 - Communication about fertility issues between the couple: {male_communication_between_couple}

**wife**.
 - Timing of infertility diagnosis: {female_age_of_diagnosis}
 - Situation of infertility treatment: {female_fertility_treatment_situation}
 - Main causes of infertility: {female_main_cause_of_infertility}
 - Financial burden of infertility treatment: {female_economic_burden_of_treatment}
 - Support from family or others: {female_support_from_family}
 - Understanding of infertility in the workplace: {female_understanding_in_workplace}
 - Communication about fertility issues between the couple: {female_communication_between_couple}

How did you feel when you were diagnosed with infertility?
What was the most difficult moment during your fertility treatment?
What comforting words did you say to each other after a failed treatment?
How do you deal with the stress of infertility?
How was communication between the couple during the treatment process?
What were the biggest conflicts you had with your fertility issues?
What efforts are you making to understand each other's feelings?
How have you talked to people around you about infertility?
How do you share the financial burden of treatment?
What have you said or done that has been the most supportive to each other?
How have you met each other's needs during fertility treatment?
Where do you get information about fertility?
Do you do hobbies to reduce the stress of infertility?
How do you respect each other's feelings?
Have you considered other solutions besides fertility treatment?
What stress-relieving activities do you engage in as a couple?
How has the couple's relationship changed over the course of treatment?
Have your social activities changed because of your fertility issues?
How do you express your support for each other?
What made you decide to try again after a failed treatment?
What kind of future do you envision for each other?
What support was most helpful during your fertility treatment?
Have you ever sought fertility counseling and what was that experience like?
Are you involved in any community activities to address fertility issues?
What are you doing to support each other's health?
What are your mutual commitments to the success of your treatment?
What are your expectations for each other during fertility treatment?
Do you feel like you have enough fertility information and support?
When have you been most grateful for each other?
Do you have any special ways as a couple to cope with infertility?

And please don't think about the questions below because they've already been asked.
{exists_questions}
    """

    def __init__(self, wife: User, husband: User):
        self.wife = wife
        self.husband = husband

    def create(self, match: Match):
        questions: List[Question] = Question.objects.filter(match=match).get()
        question_list = list(map(lambda q: q.content, questions))
