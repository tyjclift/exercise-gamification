from django.contrib import admin

# Register your models here.

from .models import UpperBody



class ChoiceInLine(admin.TabularInline):
	model = UpperBody
	#extra = 3

