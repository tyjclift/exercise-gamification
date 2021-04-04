from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import *

class IndexView(generic.TemplateView):
    template_name = 'index.html'

# class CardioView(CreateView):
#     model = Cardio
#     fields = ['running', 'biking', 'swimming', 'walking']
#     success_url = "index/"

# class LowerBodyView(CreateView):
#     model = LowerBody
#     fields = ['squats', 'lunges', 'calf_raises', 'leg_press', 'deadlifts']
#     success_url = "index/"

# https://stackoverflow.com/questions/22739701/django-save-modelform
def UpperBodyView(request):
    form = UpperBodyForm(request.POST or None)
    if form.is_valid():
        form.save()
        querey_list = UpperBody.objects.all()
        return render(request, 'index.html', {'querey_list': querey_list})
    context = {'form': form }
        
    return render(request, 'index/upperbody_form.html', context)

def CardioView(request):
    form = CardioForm(request.POST or None)
    if form.is_valid():
        form.save()
        querey_list = Cardio.objects.all()
        return render(request, 'index.html', {'querey_list': querey_list})
    context = {'form': form }
        
    return render(request, 'index/cardio_form.html', context)

def LowerBodyView(request):
    form = LowerBodyForm(request.POST or None)
    if form.is_valid():
        form.save()
        querey_list = LowerBody.objects.all()
        return render(request, 'index.html', {'querey_list': querey_list})
    context = {'form': form }
        
    return render(request, 'index/cardio_form.html', context)