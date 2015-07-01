from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect

from home import views as homeviews
from models import Doctor, Patient 

# Create your views here.

def my_auth(request):
	if request.method == 'POST':
		print 'POST'
		password = request.POST['password']
		username = request.POST['username']
		docpat = request.POST['docpat']
		next = request.POST['next']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				print 'logged in'
				if docpat == 'doc':
					print 'is doc'
					doc = get_object_or_404(Doctor, pk=user)
					doc.online = True
					doc.save()
				print 'returning view'
				return homeviews.home(request)
			else:
				return HttpResponse('DISABLED ACCOUNT')
		else:
			return HttpResponse('INVALID LOGIN')
	elif request.method == 'GET':
		print 'GET'
		context = {}
		return render(request, 'accounts/login.html', context)

def config(request):
	context = {}
	return render(request, 'accounts/config.html', context)