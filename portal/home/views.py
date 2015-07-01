from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from accounts.models import Doctor, Patient, gen_user
from django.contrib.auth.models import User 

# Create your views here.
@login_required
def home(request):
	context = {}
	username = request.user.username
	user = gen_user.objects.get(user=User.objects.get(username=username))
	context['user'] = user
	print 'rendering page'
	return render(request, 'home/landing_page.html', context)