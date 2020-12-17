from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def quizhome(request):
    return HttpResponse("Hi, Welcome to quiz")
