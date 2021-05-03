from django.db import models
from django.shortcuts import render
from django import forms
from django.contrib.auth.models import User
import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


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
    time = models.PositiveSmallIntegerField(default=0)
    distance = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(max_length=17, choices=Cardio_Types, default='running')
    date = models.DateField(default=datetime.date.today)

    current_user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )

class CardioForm(forms.ModelForm):
    class Meta:
        model = Cardio
        fields = ['type', 'time', 'distance', 'date']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'first arg is the legend of the fieldset',
                'like_website',
                'favorite_number',
                'favorite_color',
                'favorite_food',
                'notes'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )


class UpperBody(models.Model):
    reps = models.PositiveSmallIntegerField(default=0)
    sets = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(max_length=17, choices=UpperBody_Types, default='pushups')
    date = models.DateField(default=datetime.date.today)

    current_user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )

class UpperBodyForm(forms.ModelForm):
    class Meta:
        model = UpperBody
        fields = ['type','reps','sets', 'date']


class LowerBody(models.Model):
    reps = models.PositiveSmallIntegerField(default=0)
    sets = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(max_length=17, choices=LowerBody_Types, default='sqauts')
    date = models.DateField(default=datetime.date.today)

    current_user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )

class LowerBodyForm(forms.ModelForm):
    class Meta:
        model = LowerBody
        fields = ['type','reps','sets', 'date']


class FriendRequest(models.Model):
    email = models.CharField(max_length=40)
    current_user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )


class FriendRequestForm(forms.ModelForm):
    class Meta:
        model = FriendRequest
        fields = ['email']