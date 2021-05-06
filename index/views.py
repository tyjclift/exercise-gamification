from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block, FriendshipRequest
from friendship.exceptions import AlreadyExistsError, AlreadyFriendsError
from django.core.exceptions import ValidationError
import operator
from functools import cmp_to_key
from .models import *
from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
from friendship.exceptions import *

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
    weather_multipler = 1
    context = {}
    if request.user.is_authenticated:

        # change city to test precipitation feature
        city = 'Charlottesville'

        # source contain JSON data from API 
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=9e6149bb94b5fc22796dfe758638c877').read()
        
        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        isBadWeather = None
        if (str(list_of_data['weather'][0]['main']) == ('Rain' or 'Snow' or 'Extreme')):
            isBadWeather = True

        if isBadWeather:
            weather_multipler = 1.5

        print("OG weather mult: ", weather_multipler)
        precipitation = ""
        if(str(list_of_data['weather'][0]['main']) == ('Rain')):
            precipitation = "Rain detected in Charlottesville! You'll receive bonus points for running or biking today!"
        elif(str(list_of_data['weather'][0]['main']) == ('Snow')):
            precipitation = "Snow detected in Charlottesville! You'll receive bonus points for running or biking today!"
        elif(str(list_of_data['weather'][0]['main']) == ('Extreme')):
            precipitation = "Extreme weather detected in Charlottesville! For your safety, do not exercise outside!"
        else:
            precipitation = "No precipitation detected."

            
        total_points = get_total_points(UpperBody.objects.filter(current_user=request.user),LowerBody.objects.filter(current_user=request.user),Cardio.objects.filter(current_user=request.user))
        curr_level = get_level(total_points)
        context = {
            'cardio_query_list': Cardio.objects.filter(current_user=request.user)[::-1],
            'upper_query_list': UpperBody.objects.filter(current_user=request.user)[::-1],
            'lower_query_list': LowerBody.objects.filter(current_user=request.user)[::-1],
            'cardio_points': get_points_by_type(Cardio.objects.filter(current_user=request.user)[::-1],"cardio"),
            'upper_points': get_points_by_type(UpperBody.objects.filter(current_user=request.user)[::-1], "upper"),
            'lower_points': get_points_by_type(LowerBody.objects.filter(current_user=request.user)[::-1], "lower"),
            'total_points': total_points,
            'curr_level': curr_level,
            'pts_to_next_level': get_pts_to_next(curr_level),
            'pct_to_next_level': get_pct_to_next(total_points, curr_level),
            'weather': str(list_of_data['weather'][0]['main']),
            'precipitation': precipitation,
            'temp': str(list_of_data['main']['temp']) + ' \N{DEGREE SIGN}F',
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']) + '%',
            'wind': str(list_of_data['wind']['speed']) + ' mph',
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

def SocialView(request):
    print("Im in the social view")
    form = FriendRequestForm(request.POST or None)
    emails = []
    accept_btn_list = []
    reject_btn_list =[]
    remove_btn_list =[]
    friends_points={}
    friends_list=[]
    friends_usernames = []
    if len(User.objects.values())>0:
        for i in range(len(User.objects.values())):
            #print(User.objects.values()[i])
            emails.append((User.objects.values()[i]['email']))

    for my_request in Friend.objects.requests(user=request.user):
        accept_btn_list.append("accept_" + my_request.from_user.email)
        reject_btn_list.append("reject_" + my_request.from_user.email)

    for friend in Friend.objects.friends(request.user):
        friends_usernames.append(friend.username)
        friends_list.append(friend)
        remove_btn_list.append("remove_" + friend.email)
        upper = UpperBody.objects.filter(current_user=friend)
        lower = LowerBody.objects.filter(current_user=friend)
        cardio = Cardio.objects.filter(current_user=friend)
        friends_points[friend.username]=get_total_points(upper,lower,cardio)
    friends_points[request.user.username + " (you)"]= get_total_points(UpperBody.objects.filter(current_user=request.user),
                                                            LowerBody.objects.filter(current_user=request.user),
                                                            Cardio.objects.filter(current_user=request.user))
    friends_ordered_by_points = sorted(friends_points.items(), key=operator.itemgetter(1), reverse=True)
    if form.is_valid():
        form_user = form.save(commit=False)
        form_user.current_user = request.user
        form_user.save()
        form.save()
        print("Finished form save")
    if request.method == 'POST' and 'email' in request.POST.keys():
        #print(request.POST)
        #print(Friend.objects.unrejected_requests(user=request.user))
        requested_email = request.POST['email']
        #print(requested_email)
        if requested_email in emails and requested_email!=request.user.email:
            other_user = User.objects.get(email=requested_email)
            try:
                Friend.objects.add_friend(
                    request.user,  # The sender
                    other_user,  # The recipient
                    message='Hi! I would like to add you')
                ctx = {
                    'requested_username': other_user.username,}
            except AlreadyExistsError:
                ctx = {
                    'requested_username': other_user.username, }
                return render(request, 'index/already_sent.html', context=ctx)
            except AlreadyFriendsError:
                ctx = {
                    'requested_username': other_user.username, }
                return render(request, 'index/already_friends.html', context=ctx)

            return render(request, 'index/sent.html', context = ctx)
    if request.method == 'POST' and 'Accept' in request.POST.values():
        for btn in accept_btn_list:
            if btn in request.POST.keys():
                email = btn[7:]
                user = User.objects.get(email__exact=email)
                friend_request = FriendshipRequest.objects.get(from_user=user,to_user=request.user)
                print(friend_request.from_user.email)
                friend_request.accept()
                ctx = {
                    'friend':user.username,
                }
                for friend in Friend.objects.friends(request.user):
                    print(friend.username)
                for friend2 in Friend.objects.friends(user):
                    print(friend2.username)
                print(Friend.objects.unrejected_requests(user=request.user))
                return render(request, 'index/accepted.html', context=ctx)
    if request.method == 'POST' and 'Reject' in request.POST.values():
        for btn in reject_btn_list:
            if btn in request.POST.keys():
                email = btn[7:]
                user = User.objects.get(email__exact=email)
                friend_request = FriendshipRequest.objects.get(from_user=user,to_user=request.user)
                print(Friend.objects.unrejected_requests(user=request.user))
                friend_request.reject()
                print(Friend.objects.requests(user=request.user))
                ctx = {
                    'friend': user.username,
                }

                return render(request, 'index/rejected.html', context=ctx)
    if request.method == 'POST' and 'Remove' in request.POST.values():
        for btn in remove_btn_list:
            if btn in request.POST.keys():
                email =btn[7:]
                other_user = User.objects.get(email__exact=email)
                print(other_user)
                Friend.objects.remove_friend(request.user, other_user)
                ctx = ctx = {
                    'friend':other_user.username,
                }
                return render(request, 'index/removed.html', context=ctx)
    for my_request in Friend.objects.sent_requests(user=request.user):
        has_rejected = Friend.objects.rejected_requests(user=my_request.to_user)
        for rejects in has_rejected:
            if rejects.from_user == request.user:
                #sent_requests.remove(my_request)
                print("Friendship request from "+ request.user.username + "was rejected by "+ my_request.to_user.email)
                mean_user = User.objects.get(email__exact=my_request.to_user.email)
                FriendshipRequest.objects.filter(
                    from_user=request.user, to_user=mean_user
                ).delete()
    #sent_requests = Friend.objects.sent_requests(user=request.user)

    ctx1 = {'form': form,
            'sent_requests': Friend.objects.sent_requests(user=request.user),
            'pending_requests':Friend.objects.unrejected_requests(user=request.user),
            'has_rejected':Friend.objects.rejected_requests(user=request.user),
            'friends_lb': friends_ordered_by_points,
            'friends': friends_list,
            }

    print("Your Friends usernames:", friends_usernames)
    print("Your Friend Objects:", friends_list)
    print("Pending requests:", Friend.objects.unrejected_requests(user=request.user))
    print("Sent requests:", Friend.objects.sent_requests(user=request.user))
    print("Im at the end of social view about to render")
    return render(request, 'index/social.html', context=ctx1)

def comparator(user_1, user_2):
	return user_2["points"] - user_1["points"]

def UserListView(request):
	all_users = User.objects.all()
	# if all users is empty then show nothing

	total_points = []
	for x in all_users:
		points = get_total_points(UpperBody.objects.filter(current_user=x),
				LowerBody.objects.filter(current_user=x),
				Cardio.objects.filter(current_user=x))
		total_points.append({
			"user": x.first_name + " " + x.last_name,
			"points": points,
			"level": get_level(points)
		})

	total_points.sort(key=cmp_to_key(comparator))

	list_to_pass = []
	count = 0
	for i in range(len(total_points)):
		if count == 5:
			break
		list_to_pass.append(total_points[i])
		count += 1

	context = {
		"database_list": list_to_pass
	}

	return render(request, 'index/database_list.html', context)

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
        if(xp < ((500 * (level ** 2) - (500 * level))) * 10):
            return level - 1
            break
    return 1000 # max level is 1000

def get_pts_to_next(curr_level):
    level = curr_level + 1
    if (level >= 1000):
        return 0 # max level of 1000 has been reached
    else:
        return ((500 * (level ** 2) - (500 * level)) * 10)


def get_pct_to_next(total_points, curr_level):
    pct = total_points / get_pts_to_next(curr_level) * 100
    return round(pct)

#print(Friend.objects.friends(request.user))
