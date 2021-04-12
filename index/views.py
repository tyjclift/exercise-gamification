from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import *

mult_vals = {
    'Running': 3,
    'Biking': 2.63,
    'Swimming': 2,
    'Walking': 1,
    'Pushups': 1,
    'Pullups': 3.5,
    'Back row': 3,
    'Bicep curls': 1.25,
    'Tricep Extensions': 1.25,
    'Squats': .9,
    'Lunges': .95,
    'Calf Raises': .85,
    'Leg Press': 1.75,
    'Deadlifts': 2.25,
}

def IndexView(request):
    context = {}
    if request.user.is_authenticated:
        total_points = get_total_points(UpperBody.objects.filter(current_user=request.user),LowerBody.objects.filter(current_user=request.user),Cardio.objects.filter(current_user=request.user))
        curr_level = get_level(total_points)
        context = {
            'cardio_query_list': Cardio.objects.filter(current_user=request.user),
            'upper_query_list': UpperBody.objects.filter(current_user=request.user),
            'lower_query_list': LowerBody.objects.filter(current_user=request.user),
            'cardio_points': get_points_by_type(Cardio.objects.filter(current_user=request.user),"cardio"),
            'upper_points': get_points_by_type(UpperBody.objects.filter(current_user=request.user), "upper"),
            'lower_points': get_points_by_type(LowerBody.objects.filter(current_user=request.user), "lower"),
            'total_points': total_points,
            'curr_level': curr_level,
            'pts_to_next_level': get_pts_to_next(curr_level),
            'pct_to_next_level': get_pct_to_next(total_points, curr_level),
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


def get_points_by_type(query_list,type):
    points_list=[]
    if type == "cardio":
        for data in query_list:
            value = round(((data.time)**1.25 * (data.distance + data.distance/max(1,data.time))*mult_vals[data.type]))
            points_list.append(value)
        return points_list
        
    elif type == "upper":
        for data in query_list:
            value = round(data.sets * data.reps * mult_vals[data.type])
            points_list.append(value)
        return points_list
    elif type == "lower":
        for data in query_list:
            value = round(data.sets * data.reps * mult_vals[data.type])
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

# Based on D&D level system:
# xp_to_next = 500 * (level ** 2) - (500 * level)
# so 10000 to get to level 2, 30000 to get to level 3, 60000 to get to level 4, and so on

def get_level(xp):
    if(xp < 0):
        print("error: negative xp")
    for level in range (1, 1000):
        print("entering loop")
        print("level: ", level)
        print("xp: ", xp, "/", (500 * (level ** 2) - (500 * level)))
        if(xp < ((500 * (level ** 2) - (500 * level))) * 10):
            print("xp < goal")
            return level - 1
            break
    return 0

def get_pts_to_next(curr_level):
    level = curr_level + 1
    return ((500 * (level ** 2) - (500 * level)) * 10)


def get_pct_to_next(total_points, curr_level):
    pct = total_points / get_pts_to_next(curr_level) * 100
    return round(pct)