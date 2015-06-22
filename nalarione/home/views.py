from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import Doctor, Patient
from django.contrib.auth.models import User 

# Create your views here.
@login_required
def home(request):
	context = {}
	username = request.user.username
	user = User.objects.get(username=username)
	first_name = user.get_short_name()
	context['first_name'] = first_name
	print 'rendering page'
	return render(request, 'home/landing_page.html', context)