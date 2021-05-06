# Generated by Django 3.1.7 on 2021-05-04 14:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UpperBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.PositiveSmallIntegerField(default=0)),
                ('sets', models.PositiveSmallIntegerField(default=0)),
                ('type', models.CharField(choices=[('Pushups', 'PUSHUPS'), ('Pullups', 'PULLUPS'), ('Back row', 'BACK_ROW'), ('Bicep curls', 'BICEP_CURLS'), ('Tricep Extensions', 'TRICEP_EXTENSIONS')], default='pushups', max_length=17)),
                ('date', models.DateField(default=datetime.date.today)),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LowerBody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reps', models.PositiveSmallIntegerField(default=0)),
                ('sets', models.PositiveSmallIntegerField(default=0)),
                ('type', models.CharField(choices=[('Squats', 'SQUATS'), ('Lunges', 'LUNGES'), ('Calf Raises', 'CALF_RAISES'), ('Leg Press', 'LEG_PRESS'), ('Deadlifts', 'DEADLIFTS')], default='sqauts', max_length=17)),
                ('date', models.DateField(default=datetime.date.today)),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cardio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.PositiveSmallIntegerField(default=0)),
                ('distance', models.PositiveSmallIntegerField(default=0)),
                ('type', models.CharField(choices=[('Running', 'RUNNING'), ('Biking', 'BIKING'), ('Swimming', 'SWIMMING'), ('Walking', 'WALKING')], default='running', max_length=17)),
                ('date', models.DateField(default=datetime.date.today)),
                ('current_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]