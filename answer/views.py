from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Answer
from question.models import Question
from .forms import AnswerForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


def submit_answer(APIView):
    
    def post(self, request):
        question_id = request.data.get("question_id")
        question = get_object_or_404(Question, pk=question_id)

        
        form = AnswerForm(request.data)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return Response({"detail": "Answer submitted successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)