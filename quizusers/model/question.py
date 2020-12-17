from django.db import models
from datetime import datetime


class QuizQuestions(models.Model):
    quiztitle = models.CharField(max_length = 255)
    question = models.CharField('Quiz Question', max_length=200)
    created_date = models.DateTimeField('Question Created Date', default=datetime.now())