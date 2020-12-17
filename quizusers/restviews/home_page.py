from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def quizhome(request):
    return render(request, 'quizindex.html')