from django.urls import path
from . import views

urlpatterns = [
    path("submit/<int:question_id>/", views.submit_answer, name="submit_answer"),
]
