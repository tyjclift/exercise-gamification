from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView
from django import forms
import datetime

# Create your models here.

Cardio_Types = (
        ('Running', 'RUNNING'),
        ('Biking', 'BIKING'),
        ('Swimming', 'SWIMMING'),
        ('Walking', 'WALKING'),
)
UpperBody_Types = (
        ('Pushups', 'PUSHUPS'),
        ('Pullups', 'PULLUPS'),
        ('Back row', 'BACK_ROW'),
        ('Bicep curls', 'BICEP_CURLS'),
        ('Tricep Extensions', 'TRICEP_EXTENSIONS'),
)
LowerBody_Types = (
        ('Squats', 'SQUATS'),
        ('Lunges', 'LUNGES'),
        ('Calf Raises', 'CALF_RAISES'),
        ('Leg Press', 'LEG_PRESS'),
        ('Deadlifts', 'DEADLIFTS'),
)


class Cardio(models.Model):
    # running = models.CharField(max_length=10)
    # biking = models.CharField(max_length=10)
    # swimming = models.CharField(max_length=10)
    # walking = models.CharField(max_length=10)
    time = models.PositiveSmallIntegerField(default=0)
    distance = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(max_length=17, choices=Cardio_Types, default='running')
    date = models.DateField(default=datetime.date.today)

class CardioForm(forms.ModelForm):
    class Meta:
        model = Cardio
        fields = ['type','time', 'distance', 'date']

class LowerBody(models.Model):
    # squats = models.CharField(max_length=4)
    # lunges = models.CharField(max_length=4)
    # calf_raises = models.CharField(max_length=4)
    # leg_press = models.CharField(max_length=4)
    # deadlifts = models.CharField(max_length=4)
    reps = models.PositiveSmallIntegerField(default=0)
    sets = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(max_length=17, choices=LowerBody_Types, default='sqauts')
    date = models.DateField(default=datetime.date.today)

class LowerBodyForm(forms.ModelForm):
    class Meta:
        model = LowerBody
        fields = ['type','reps','sets', 'date']

class UpperBody(models.Model):
    # pushups = models.CharField(max_length=4)
    # pullups = models.CharField(max_length=4)
    # back_row = models.CharField(max_length=4)
    # bicep_curl = models.CharField(max_length=4)
    # tricep_extension = models.CharField(max_length=4)
    reps = models.PositiveSmallIntegerField(default=0)
    sets = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(max_length=17, choices=UpperBody_Types, default='pushups')
    date = models.DateField(default=datetime.date.today)

class UpperBodyForm(forms.ModelForm):
    class Meta:
        model = UpperBody
        fields = ['type','reps','sets', 'date']