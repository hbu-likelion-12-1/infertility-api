from django import forms
from .models import QuestionComment

class QuestionCommentForm(forms.ModelForm):

    class Meta:
        model = QuestionComment
        fields = ['content']
