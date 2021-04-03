from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import *

class IndexView(generic.TemplateView):
    template_name = 'index.html'

class CardioView(CreateView):
    model = Cardio
    fields = ['running', 'biking', 'swimming', 'walking']
    success_url = "index/"

class LowerBodyView(CreateView):
    model = LowerBody
    fields = ['squats', 'lunges', 'calf_raises', 'leg_press', 'deadlifts']
    success_url = "index/"

# class UpperBodyView(CreateView):
#     model = UpperBody
#     fields = ['pushups', 'pullups', 'back_row', 'bicep_curl', 'tricep_extension']
#     success_url = "index/"


def UpperBodyView(request):
    form = UpperBodyForm(request.POST or None)
    if form.is_valid():
        form.save()
        querey_list = UpperBody.objects.all()
        return render(request, 'index.html', {'querey_list': querey_list})
    context = {'form': form }
        
    return render(request, 'index/upperbody_form.html', context)

# def parse_thoughts(request):
# 	thoughts_var = Thoughts(title_text=request.POST['title_text'], 
# 		deep_thought_text=request.POST['deep_thought_text'])
# 	thoughts_var.save()

# 	return HttpResponseRedirect(reverse('polls:thoughts'))


# def upper_body_list(request):
# 	querey_list = UpperBodyForm.objects.all()
# 	print(querey_list)
# 	return render(request, 'index.html', {'querey_list': querey_list})



# class CreateUpperBodyView(CreateView):
#     model = UpperBody
#     form_class = UpperBodyForm
#     # template_name = 'index/upperbody_form.html'
#     success_url = '/index'

# class ResultView(generic.ListView):
#     # model = 
