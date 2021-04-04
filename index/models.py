from django.db import models
from django import forms

# Create your models here.

class Cardio(models.Model):
    running = models.CharField(max_length=10)
    biking = models.CharField(max_length=10)
    swimming = models.CharField(max_length=10)
    walking = models.CharField(max_length=10)

class LowerBody(models.Model):
    squats = models.CharField(max_length=4)
    lunges = models.CharField(max_length=4)
    calf_raises = models.CharField(max_length=4)
    leg_press = models.CharField(max_length=4)
    deadlifts = models.CharField(max_length=4)


# class Upper(models.Model):
#     upper_workout = models.CharField(choices=UPPER_WORKOUTS)
#     workout_counter = models.SmallIntegerField(default=0)

class UpperBody(models.Model):
    UPPER_WORKOUTS = (('pushups', 'pushups'),)
    upper_workout = models.CharField(max_length=10, choices=UPPER_WORKOUTS, default='pushups')
    reps_count = models.SmallIntegerField(default=0)
    sets_count = models.SmallIntegerField(default=0)
    reps = models.SmallIntegerField(default=0)
    sets = models.SmallIntegerField(default=0)
    # reps = models.SmallIntegerField(max_length=4, default='')
    # sets = models.SmallIntegerField(max_length=4, default='')

class UpperBodyForm(forms.ModelForm):
    class Meta:
        model = UpperBody
        fields = ['sets','reps']

# class UpperBody(models.Model):
#     pushups = models.CharField(max_length=4)
#     # pullups = models.CharField(max_length=4)
#     # back_row = models.CharField(max_length=4)
#     # bicep_curl = models.CharField(max_length=4)
#     # tricep_extension = models.CharField(max_length=4)
