from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.db.models import F
from django.views.generic.edit import CreateView

from .models import *

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class CardioView(CreateView):
    model = Cardio
    fields = ['running', 'biking', 'swimming', 'walking']
    success_url = "/index"

class LowerBodyView(CreateView):
    model = LowerBody
    fields = ['squats', 'lunges', 'calf_raises', 'leg_press', 'deadlifts']
    success_url = "/index"


def UpperBodyView(request):
    form = UpperBodyForm(request.POST or None)
    if form.is_valid():
        cd = form.cleaned_data
        workout_log = UpperBody.objects.get_or_create(upper_workout='pushups')[0]
        workout_log.reps_count = F('reps_count') + cd.get('reps')
        workout_log.sets_count = F('sets_count') + cd.get('sets')
        print(workout_log.reps_count)
        context = { 'pushups':{'reps':workout_log.reps_count, 'sets':workout_log.sets_count} }

    context = {'form': form}
    return render(request, 'index.html/', context)

    # context = {'reps':workout_log.reps, 'sets':workout_log.sets}
    # return render(request, 'index.html', context)

# def UpperBodyView(request):
#     form = UpperBodyForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         querey_list = UpperBody.objects.all()
#         return render(request, 'index.html', {'querey_list': querey_list})
#     context = {'form': form }
        
#     return render(request, 'index/upperbody_form.html', context)

# class UpperBodyView(CreateView):
#     model = UpperBody
#     fields = ['pushups']
#     success_url = "/index"

# class ResultView(generic.ListView):
#     # model = 
