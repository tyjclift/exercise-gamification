from django.db import models

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

class UpperBody(models.Model):
    pushups = models.CharField(max_length=4)
    pullups = models.CharField(max_length=4)
    back_row = models.CharField(max_length=4)
    bicep_curl = models.CharField(max_length=4)
    tricep_extension = models.CharField(max_length=4)
