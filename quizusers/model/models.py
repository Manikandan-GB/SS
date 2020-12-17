from django.db import models

class QuizQuestions(models.Model):
    question = models.CharField('Quiz Question', max_length=200)
    created_date = models.DateTimeField('Question Created Date')

class QuizAnswers(models.Model):
    answer = models.CharField('Quiz Answer', max_length=200 )
    question = models.ForeignKey(QuizQuestions, on_delete=models.CASCADE)
    created_date = models.DateTimeField('Answer Created Date')


class Users(models.Model):
    user_name = models.CharField('User Name', max_length=200)
    user_email = models.EmailField('User Email',max_length=200)
    user_created_on = models.DateTimeField('User Created Time')

class UserScores(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    user_score = models.IntegerField("User Score", max_length=10)
    created_on = models.DateTimeField("Score CreatedDate")