from django.db import models
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView
from django import forms
# Create your models here.

Cardio_Types = (
        ('running', 'RUNNING'),
        ('biking', 'BIKING'),
        ('swimming', 'SWIMMING'),
        ('walking', 'WALKING'),
    )
UpperBody_Types = (
        ('pushups', 'PUSHUPS'),
        ('pullups', 'PULLUPS'),
        ('back_row', 'BACK_ROW'),
        ('bicep_curls', 'BICEP_CURLS'),
        ('tricep_extensions', 'TRICEP_EXTENSIONS'),
    )
LowerBody_Types = (
        ('sqauts', 'SQUATS'),
        ('lunges', 'LUNGES'),
        ('calf_raises', 'CALF_RAISES'),
        ('leg_press', 'LEG_PRESS'),
        ('deadlifts', 'DEADLIFTS'),
    )

class Cardio(models.Model):
    # running = models.CharField(max_length=10)
    # biking = models.CharField(max_length=10)
    # swimming = models.CharField(max_length=10)
    # walking = models.CharField(max_length=10)
    time = models.CharField(max_length=4, default='')
    distance = models.CharField(max_length=4, default='')
    type = models.CharField(max_length=17, choices=Cardio_Types, default='running')

class CardioForm(forms.ModelForm):
    class Meta:
        model = Cardio
        fields = ['type','time', 'distance']

class LowerBody(models.Model):
    #squats = models.CharField(max_length=4)
    #lunges = models.CharField(max_length=4)
    #calf_raises = models.CharField(max_length=4)
    #leg_press = models.CharField(max_length=4)
    #deadlifts = models.CharField(max_length=4)
    reps = models.CharField(max_length=4, default='')
    sets = models.CharField(max_length=4, default='')
    type = models.CharField(max_length=17, choices=LowerBody_Types, default='sqauts')

class LowerBodyForm(forms.ModelForm):
    class Meta:
        model = LowerBody
        fields = ['type','sets','reps']


class UpperBody(models.Model):
    # pushups = models.CharField(max_length=4)
    # pullups = models.CharField(max_length=4)
    # back_row = models.CharField(max_length=4)
    # bicep_curl = models.CharField(max_length=4)
    # tricep_extension = models.CharField(max_length=4)
    reps = models.CharField(max_length=4, default='')
    sets = models.CharField(max_length=4, default='')
    type = models.CharField(max_length=17, choices=UpperBody_Types, default='pushups')

class UpperBodyForm(forms.ModelForm):
    class Meta:
        model = UpperBody
        fields = ['type','sets','reps']
