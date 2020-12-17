from django.db import models
from .question import QuizQuestions
from datetime import datetime

class QuestionAnswersOption(models.Model):
    answer_option_1 = models.CharField('Question Answer Option 1', max_length=200 )
    answer_option_2 = models.CharField('Question Answer Option 2', max_length=200)
    answer_option_3 = models.CharField('Question Answer Option 3', max_length=200)
    answer_option_4 = models.CharField('Question Answer Option 4', max_length=200)
    question = models.ForeignKey(QuizQuestions, on_delete=models.CASCADE)
    created_date = models.DateTimeField('Answer Created Date', default=datetime.now())

class QuestionAnswers(models.Model):
    question_answer = models.IntegerField('Question Correct Answer')
    question = models.ForeignKey(QuizQuestions, on_delete=models.CASCADE)
    created_date = models.DateTimeField('Answer Created Date', default=datetime.now())
