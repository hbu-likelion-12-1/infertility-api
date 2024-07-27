from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, QuestionComment
from .forms import QuestionCommentForm

def question_detail(request, question_id):
    question = get_object_or_404(Question, id = question_id)
    comments = question.question_comments.all()

    if request.method == 'POST':
        form = QuestionCommentForm(requst.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = request.user
            comment.question = question
            comment.save()
            return redirect('question_detail', question_id = question.id)
        else:
            form = QuestionCommentForm()

        context = {
            'question' : question,
            'comments' : comments,
            'form' : form
        }

        