from django.contrib import admin

from .model import QuizQuestions, QuizAnswers

admin.site.register(QuizQuestions)
admin.site.register(QuizAnswers)
