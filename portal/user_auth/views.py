from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_page(request):
	context = {}
	return render(request, 'user_auth/login.html',context)

def user_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return landing_page(request)
        else:
        	return HttpResponse("DISABLED ACCOUNT")
            # Return a 'disabled account' error message
    else:
    	return HttpResponse("INVALID LOGIN")
        # Return an 'invalid login' error message.

def user_create(request):
	return HttpResponse("Coming soon!")

def landing_page(request):
	context = {}
	return render(request, 'user_auth/landing_page.html', context)