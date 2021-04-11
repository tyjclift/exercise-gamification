from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import *

def IndexView(request):
    context = {}
    if request.user.is_authenticated:
        context = {
            'cardio_query_list': Cardio.objects.filter(current_user=request.user),
            'upper_query_list': UpperBody.objects.filter(current_user=request.user),
            'lower_query_list': LowerBody.objects.filter(current_user=request.user),
            'cardio_points': get_points_by_type(Cardio.objects.filter(current_user=request.user),"cardio"),
            'upper_points': get_points_by_type(UpperBody.objects.filter(current_user=request.user), "upper"),
            'lower_points': get_points_by_type(LowerBody.objects.filter(current_user=request.user), "lower"),
            'total_points': get_total_points(UpperBody.objects.filter(current_user=request.user),LowerBody.objects.filter(current_user=request.user),Cardio.objects.filter(current_user=request.user))
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


def get_points_by_type(querey_list,type):
    points_list=[]
    if type == "upper":
        for data in querey_list:
            if data.type == "Pushups":
                mult = 1
            elif data.type == "Pullups":
                mult = 3.5
            elif data.type == "Back row":
                mult = 3
            else:
                mult = 1.25
            value = round(data.sets * data.reps * mult)
            points_list.append(value)
        return points_list
    elif type == "cardio":
        for data in querey_list:
            if data.type == "Running":
                mult = 3
            elif data.type == "Biking":
                mult = 2.63
            elif data.type == "Swimming":
                mult = 2
            elif data.type == "Walking":
                mult = 1
            else:
                print("error something went wrong.")
            value = round(((data.time)**1.25 * (data.distance + data.distance/data.time)*mult))
            points_list.append(value)
        return points_list
    elif type == "lower":
        for data in querey_list:
            if data.type == "Squats":
                mult = .9
            elif data.type == "Lunges":
                mult = .95
            elif data.type == "Calf Raises":
                mult = .85
            elif data.type == "Leg Press":
                mult = 1.75
            elif data.type == "Deadlifts":
                mult = 2.25
            else:
                print("error something went wrong.")
            value = round(data.sets * data.reps * mult)
            points_list.append(value)
        return points_list
    else:
        print("invalid call")
        return points_list
def get_total_points(upper,lower,cardio):
    total = 0
    upper_list = get_points_by_type(upper,"upper")
    lower_list = get_points_by_type(lower, "lower")
    cardio_list = get_points_by_type(cardio, "cardio")
    for x in upper_list:
        total+=x
    for x in lower_list:
        total+=x
    for x in cardio_list:
        total+=x
    return total