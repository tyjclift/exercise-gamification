from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import *

def IndexView(request):
    context = {
        'cardio_query_list': Cardio.objects.filter(current_user=request.user),
        'upper_query_list': UpperBody.objects.filter(current_user=request.user),
        'lower_query_list': LowerBody.objects.filter(current_user=request.user),
    }
    return render(request, 'index/index.html', context)

# https://stackoverflow.com/questions/22739701/django-save-modelform
def CardioView(request):
    form = CardioForm(request.POST or None)
    if form.is_valid():
        form_user = form.save(commit=False)
        form_user.current_user = request.user
        form_user.save()
        form.save()
        return redirect(IndexView)

    context = {'form': form}
    return render(request, 'index/cardio_form.html', context)


def UpperBodyView(request):
    form = UpperBodyForm(request.POST or None)
    if form.is_valid():
        form_user = form.save(commit=False)
        form_user.current_user = request.user
        form_user.save()
        form.save()
        return redirect(IndexView)

    context = {'form': form}
    return render(request, 'index/upperbody_form.html', context)


def LowerBodyView(request):
    form = LowerBodyForm(request.POST or None)
    if form.is_valid():
        form_user = form.save(commit=False)
        form_user.current_user = request.user
        form_user.save()
        form.save()
        return redirect(IndexView)
    
    context = {'form': form}
    return render(request, 'index/lowerbody_form.html', context)