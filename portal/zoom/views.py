from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.utils.timezone import get_current_timezone

from accounts.models import Doctor, Patient
from django.contrib.auth.models import User

import requests

# Create your views here.
def schedule(request):
	context = {}
	return render(request, 'zoom/schedule.html', context)

@login_required
def scheduled(request):
	api_key = '_U9QcLjZQuCJQfRLvREdxQ'
	api_secret = 'H8CjFAZfkH6hTiKCzF9rDG2mDemFeGI7LnWf'

	datetime = request.POST['datetime'] + ':00Z'
	duration = request.POST['duration']

	username = None
	zoom_id = None
	context = {}

	zoom_id = Patient.objects.get(user=User.objects.get(username=request.user.username)).zoom_id

	url = 'https://api.zoom.us/v1/meeting/create?api_key=' + api_key + '&api_secret=' + api_secret + '&data_type=JSON&host_id=' + zoom_id + '&topic=appointment&type=2&start_time=' + datetime + '&duration=' + duration + '&timezone=EST' 
	r = requests.post(url)

	if 'start_url' in r.json():
		start_url = r.json()['start_url']
		print start_url
		# doc_user = User.objects.get(username=request.POST['doctor'])
		# doc_user.email_user('Appointment Scheduled', 'A patient has scheduled an appointment with you at ' + datetime + 'EST. You can go to the following address to get to the meeting: ' + r.json()['join_url'])
		# User.objects.get(username=request.user.username).email_user('Appointment Scheduled', 'Your appointment has been scheduled for ' + datetime + 'EST. You can go to the following address to get to the meeting: ' + r.json()['start_url'])
		context = {'start' : start_url}
		return render(request, 'zoom/scheduled.html', context)
	else:
		context = {'info' : r.json()}
		return render(request, 'zoom/error.html', context)

@login_required
def zoom(request):
	if request.method == 'GET':
		doctor_list = Doctor.objects.filter(online=True)
		docs_avail = (len(doctor_list) > 0)
		context = {'doczoom' : 'doc' , 'doctor_list' : doctor_list, 'docs_avail' : docs_avail}
		return render(request, 'zoom/zoom.html', context)
	elif request.method == 'POST':
		api_key = '_U9QcLjZQuCJQfRLvREdxQ'
		api_secret = 'H8CjFAZfkH6hTiKCzF9rDG2mDemFeGI7LnWf'

		username = None
		zoom_id = None
		context = {}

		# zoom_id = Patient.objects.get(user=User.objects.get(username=request.user.username)).zoom_id

		url = 'https://api.zoom.us/v1/meeting/create?api_key=' + api_key + '&api_secret=' + api_secret + '&data_type=JSON&host_id=' + zoom_id + '&topic=instappointment&type=1' 
		r = requests.post(url)

		if 'start_url' in r.json():
			start_url = r.json()['start_url']
			doc_user = User.objects.get(username=request.POST['doctor'])
			# doc_user.email_user('Instappointment Request', 'A patient is waiting for you at the following address: ' + r.json()['join_url'])
			context = {'doczoom' : 'zoom', 'start' : start_url}
			return render(request, 'zoom/zoom.html', context)
		else:
			context = {'info' : r.json()}
			return render(request, 'zoom/error.html', context)


# @login_required
# def zoom(request):
# 	api_key = '_U9QcLjZQuCJQfRLvREdxQ'
# 	api_secret = 'H8CjFAZfkH6hTiKCzF9rDG2mDemFeGI7LnWf'

# 	username = None
# 	zoom_id = None
# 	context = {}

# 	zoom_id = Patient.objects.get(user=User.objects.get(username=request.user.username)).zoom_id

# 	url = 'https://api.zoom.us/v1/meeting/create?api_key=' + api_key + '&api_secret=' + api_secret + '&data_type=JSON&host_id=' + zoom_id + '&topic=instappointment&type=1' 
# 	r = requests.post(url)

# 	if 'start_url' in r.json():
# 		start_url = r.json()['start_url']
# 		doc_user = User.objects.get(username=request.POST['doctor'])
# 		# doc_user.email_user('Instappointment Request', 'A patient is waiting for you at the following address: ' + r.json()['join_url'])
# 		context = {'start' : start_url}
# 		return render(request, 'zoom/zoom.html', context)
# 	else:
# 		context = {'info' : r.json()}
# 		return render(request, 'zoom/error.html', context)