from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello CS3240! You are at the Exercise Gamification Index!")

