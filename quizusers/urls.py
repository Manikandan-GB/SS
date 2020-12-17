from django.urls import path

from .restviews import quizhome
from .restviews import quizpageview

urlpatterns = [
    path("", quizhome, name = 'quizhome'),
    path(r"quizpage/<int:id>",quizpageview)
]