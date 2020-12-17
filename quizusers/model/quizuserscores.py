from django.db import models
from .quizusers import Users
from .models import QuizQuestions
from datetime import datetime

class UserScores(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    quiz = models.ForeignKey(QuizQuestions)
    questions_answered = models.IntegerField("Total Answered Questions")
    questions_answered_correctly = models.IntegerField("Total Correct answered questions")
    user_score = models.FloatField("User Score", max_length=10)
    created_on = models.DateTimeField("Score CreatedDate", default=datetime.now())