from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import *

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class UpperBodyView(CreateView):
    model = UpperBody
    fields = ['pushups', 'pullups', 'back_row', 'bicep_curl', 'tricep_extension']
    success_url = "index/"

class LowerBodyView(CreateView):
    model = LowerBody
    fields = ['sqauts','lunges','calf_raises','leg_press','deadlifts']
    
class CardioView(CreateView):
    model = Cardio
    fields = ['running', 'biking', 'swimming', 'walking']

# class ResultView(generic.ListView):
#     # model = 
