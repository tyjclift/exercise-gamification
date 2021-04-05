from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import *

class IndexView(generic.TemplateView):
    template_name = 'index.html'

# https://stackoverflow.com/questions/22739701/django-save-modelform
def UpperBodyView(request):
    form = UpperBodyForm(request.POST or None)
    if form.is_valid():
    	form_user = form.save(commit=False)
    	form_user.current_user = request.user
    	
    	
    	form_user.save()
    	form.save()
    	
    	querey_list = UpperBody.objects.filter(current_user=request.user)
    	
    	print(querey_list)
    	return render(request, 'index/upper_list.html', {'upper_querey_list': querey_list})
    context = {'form': form}

    return render(request, 'index/upperbody_form.html', context)


def CardioView(request):
    form = CardioForm(request.POST or None)
    if form.is_valid():
        form_user = form.save(commit=False)
        form_user.current_user = request.user

        form_user.save()
        form.save()

        querey_list = Cardio.objects.filter(current_user=request.user)
        return render(request, 'index/cardio_list.html', {'cardio_querey_list': querey_list})
    context = {'form': form}

    return render(request, 'index/cardio_form.html', context)


def LowerBodyView(request):
    form = LowerBodyForm(request.POST or None)
    if form.is_valid():
        form_user = form.save(commit=False)
        form_user.current_user = request.user

        form_user.save()
        form.save()
        
        querey_list = LowerBody.objects.filter(current_user=request.user)
        return render(request, 'index/lower_list.html', {'lower_querey_list': querey_list})
    context = {'form': form}

    return render(request, 'index/lowerbody_form.html', context)