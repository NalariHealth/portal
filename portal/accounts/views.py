from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect

from home import views as homeviews
from models import Doctor, Patient, gen_user, tile_option, list_option, settings, picture
from django.contrib.auth.models import User 
from forms import PictureForm
from django.core.urlresolvers import reverse

# Create your views here.

def my_auth(request):
	if request.method == 'POST':
		print 'POST'
		password = request.POST['password']
		username = request.POST['username']
		# docpat = request.POST['docpat']
		next = request.POST['next']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				print 'logged in'
				# if docpat == 'doc':
				# 	print 'is doc'
				# 	doc = get_object_or_404(Doctor, pk=user)
				# 	doc.online = True
				# 	doc.save()
				# print 'returning view'
				return homeviews.home(request)
			else:
				return HttpResponse('DISABLED ACCOUNT')
		else:
			return HttpResponse('INVALID LOGIN')
	elif request.method == 'GET':
		print 'GET'
		context = {}
		return render(request, 'accounts/login.html', context)

def get_tile_option(title):
	if title == "none":
		return None
	else:
		return tile_option.objects.get(title=title)

def get_list_option(title):
	if title == "none":
		return None
	else:
		return list_option.objects.get(title=title)

def config(request):
	context = {}
	gu = gen_user.objects.get(user=request.user)
	if request.method == 'GET':
		context['tile_options'] = tile_option.objects.all()
		context['list_options'] = list_option.objects.all()
		tiles = [gu.settings.tile_1, gu.settings.tile_2, gu.settings.tile_3, gu.settings.tile_4, gu.settings.tile_5, gu.settings.tile_6]
		list_options = [gu.settings.list_option_1, gu.settings.list_option_2, gu.settings.list_option_3, gu.settings.list_option_4, gu.settings.list_option_5, gu.settings.list_option_6]
		s = {'tiles': [], 'list_options': []}
		for i in range(0, len(tiles)):
			if (tiles[i] != None):
				s['tiles'].append(tiles[i].title)
			else:
				s['tiles'].append("none")
		for i in range(0, len(list_options)):
			print str(i)
			print list_options[i]
			if (list_options[i] != None): 
				s['list_options'].append(list_options[i].title)
			else:
				print 'in else'
				s['list_options'].append("none")
		context['settings'] = s
		context['num_tiles'] = range(0, 6)
		context['num_list_options'] = range(0, 6)
		return render(request, 'accounts/config.html', context)
	else:
		tile_1 = get_tile_option(request.POST['tile_1'])
		tile_2 = get_tile_option(request.POST['tile_2'])
		tile_3 = get_tile_option(request.POST['tile_3'])
		tile_4 = get_tile_option(request.POST['tile_4'])
		tile_5 = get_tile_option(request.POST['tile_5'])
		tile_6 = get_tile_option(request.POST['tile_6'])
		list_option_1 = get_list_option(request.POST['list_option_1'])
		list_option_2 = get_list_option(request.POST['list_option_2'])
		list_option_3 = get_list_option(request.POST['list_option_3'])
		list_option_4 = get_list_option(request.POST['list_option_4'])
		list_option_5 = get_list_option(request.POST['list_option_5'])
		list_option_6 = get_list_option(request.POST['list_option_6'])

		if settings.objects.filter(tile_1=tile_1, tile_2=tile_2, tile_3=tile_3, tile_4=tile_4, tile_5=tile_5, tile_6=tile_6, list_option_1=list_option_1, list_option_2=list_option_2, list_option_3=list_option_3, list_option_4=list_option_4, list_option_5=list_option_5, list_option_6=list_option_6).exists():
			gu.settings = settings.objects.get(tile_1=tile_1, tile_2=tile_2, tile_3=tile_3, tile_4=tile_4, tile_5=tile_5, tile_6=tile_6, list_option_1=list_option_1, list_option_2=list_option_2, list_option_3=list_option_3, list_option_4=list_option_4, list_option_5=list_option_5, list_option_6=list_option_6)
		else:
			new_s = settings(tile_1=tile_1, tile_2=tile_2, tile_3=tile_3, tile_4=tile_4, tile_5=tile_5, tile_6=tile_6, list_option_1=list_option_1, list_option_2=list_option_2, list_option_3=list_option_3, list_option_4=list_option_4, list_option_5=list_option_5, list_option_6=list_option_6)
			new_s.save()
			gu.settings = new_s
		gu.save()
		request.method = 'GET'
		return config(request)

def photo(request):
	context = {}
	gu = gen_user.objects.get(user=request.user)
	if request.method == 'POST':
		print 'in POST'
		form = PictureForm(request.POST, request.FILES)
		if form.is_valid():
			print 'form is valid'
			newpic = picture(picfile=request.FILES['picfile'])
			newpic.save()
			gu.picture = newpic
			gu.save()
			return homeviews.home(request)
	context['picture'] = gu.picture
	context['form'] = PictureForm()
	return render(request, 'accounts/upload_photo.html', context)











