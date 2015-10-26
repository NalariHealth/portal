from django.shortcuts import render
from django.forms import ModelForm, Form, ModelChoiceField
from models import feed, practice, provider, provider_practice_rel, member 
from django.core.exceptions import MultipleObjectsReturned
from django import forms
from django.http import HttpResponse
import csv 
import datetime

class feedForm(ModelForm):
	class Meta:
		model = feed
		fields = ['name']

class practiceForm(ModelForm):
	class Meta:
		model = practice
		fields = '__all__'

class providerForm(ModelForm):
	class Meta:
		model = provider
		fields = '__all__'

class memberForm(ModelForm):
	class Meta:
		model = member
		fields = '__all__'

class pprelForm(ModelForm):
	class Meta:
		model = provider_practice_rel
		fields = '__all__'

class selectFeedForm(Form):
	feed = ModelChoiceField(queryset=feed.objects.all(), widget=forms.Select(attrs={"onChange": 'submit();'}))

class selectPracticeForm(Form):
	practice = ModelChoiceField(queryset=practice.objects.all(), widget=forms.Select(attrs={"onChange": 'submit();'}))

class selectPracticeForRelForm(Form):
	practice = ModelChoiceField(queryset=practice.objects.all(), widget=forms.Select(attrs={"onChange": 'submit();'}), label='Provider-Practice Relationship')

class selectProviderForm(Form):
	provider = ModelChoiceField(queryset=provider.objects.all(), widget=forms.Select(attrs={"onChange": 'submit();'}))

class selectMemberForm(Form):
	member = ModelChoiceField(queryset=member.objects.all(), widget=forms.Select(attrs={"onChange": 'submit();'}))

class selectPprelForm(Form):
	pprel = ModelChoiceField(queryset=provider_practice_rel.objects.all(), widget=forms.Select(attrs={"onChange": 'submit();'}))

def new(request):
	return render(request, 'feeds/select.html', {'feedForm': selectFeedForm(), 'practiceForm': selectPracticeForm(), 'providerForm': selectProviderForm(), 'memberForm': selectMemberForm(), 'pprelForm': selectPprelForm(), 'selectPracticeForRelForm': selectPracticeForRelForm()})

def new_feed(request):
	if request.method == 'POST':
		form = feedForm(request.POST)
		if form.is_valid():
			nf = form.save()
			return new(request)
	form = feedForm()
	return render(request, 'feeds/new_feed.html', {'form': form})

def new_practice(request):
	if request.method == 'POST':
		form = practiceForm(request.POST)
		if form.is_valid():
			nf = form.save()
			return new(request)
		print form.errors
	form = practiceForm()
	return render(request, 'feeds/new_practice.html', {'form': form})

def new_provider(request):
	if request.method == 'POST':
		form = providerForm(request.POST)
		if form.is_valid():
			nf = form.save()
			return new(request)
	form = providerForm()
	return render(request, 'feeds/new_provider.html', {'form': form})

def new_member(request):
	if request.method == 'POST':
		form = memberForm(request.POST)
		if form.is_valid():
			nf = form.save()
			return new(request)
	form = memberForm()
	return render(request, 'feeds/new_member.html', {'form': form})

def new_pprel(request):
	if request.method == 'POST':
		form = pprelForm(request.POST)
		if form.is_valid():
			nf = form.save()
			return new(request)
	form = pprelForm()
	return render(request, 'feeds/new_pprel.html', {'form': form})

def select_feed(request):
	if request.method == 'POST':
		f = feed.objects.get(pk=request.POST['feed'])
		original_name = request.POST['feed']
		form = feedForm(instance=f)
		return render(request, 'feeds/edit_feed.html', {'form': form, 'instance': original_name})
	else:
		return new(request)

def edit_feed(request):
	if request.method == 'POST':
		original_name = request.POST['original_name']
		original_feed = feed.objects.get(pk=original_name)
		form = feedForm(request.POST, instance=original_feed)
		if form.is_valid():
			form.save()
	return new(request)

def select_practice(request):
	if request.method == 'POST':
		p = practice.objects.get(pk=request.POST['practice'])
		original_name = request.POST['practice']
		form = practiceForm(instance=p)
		return render(request, 'feeds/edit_practice.html', {'form': form, 'instance': original_name})
	else:
		return new(request)

def edit_practice(request):
	if request.method == 'POST':
		original_practice = practice.objects.get(pk=request.POST['original_name'])
		form = practiceForm(request.POST, instance=original_practice)
		if form.is_valid():
			form.save()
	return new(request)

def select_provider(request):
	if request.method == 'POST':
		p = provider.objects.get(pk=request.POST['provider'])
		original_id = request.POST['provider']
		form = providerForm(instance=p)
		return render(request, 'feeds/edit_provider.html', {'form': form, 'instance': original_id})
	else:
		return new(request)

def edit_provider(request):
	if request.method == 'POST':
		original_provider = provider.objects.get(pk=request.POST['original_name'])
		form = providerForm(request.POST, instance=original_provider)
		if form.is_valid():
			form.save()
	return new(request)

def select_member(request):
	if request.method == 'POST':
		m = member.objects.get(pk=request.POST['member'])
		original_id = request.POST['member']
		form = memberForm(instance=m)
		return render(request, 'feeds/edit_member.html', {'form': form, 'instance': original_id})
	else:
		return new(request)

def edit_member(request):
	if request.method == 'POST':
		original_member = member.objects.get(pk=request.POST['original_name'])
		form = memberForm(request.POST, instance=original_member)
		if form.is_valid():
			form.save()
	return new(request)

def select_practice_for_rel(request):
	if request.method == 'POST':
		p = practice.objects.get(pk=request.POST['practice'])
		rels = provider_practice_rel.objects.filter(practice=p)
		return render(request, 'feeds/edit_pprels.html', {'practice': p, 'rels': rels})
	return new(request)

def delete_rel(request):
	if request.method == 'POST':
		rel = provider_practice_rel.objects.get(pk=request.POST['rel'])
		practice = rel.practice.id
		rel.delete()
		request.POST['practice'] = practice
		return select_practice_for_rel(request)
	return new(request)

def select_rel(request):
	if request.method == 'POST':
		r = provider_practice_rel.objects.get(pk=request.POST['rel'])
		original_id = request.POST['rel']
		form = pprelForm(instance=r)
		return render(request, 'feeds/edit_rel.html', {'form': form, 'instance': original_id})
	return new(request)

def edit_rel(request):
	if request.method == 'POST':
		original_rel = provider_practice_rel.objects.get(pk=request.POST['original_name'])
		form = pprelForm(request.POST, instance=original_rel)
		if form.is_valid():
			form.save()
	return new(request)

def view_feed(request):
	if request.method == 'POST':
		f = feed.objects.get(pk=request.POST['feed'])
		practices = practice.objects.filter(feed=f)
		practice_providers = {}
		for p in practices:
			providers = []
			rels = provider_practice_rel.objects.filter(practice=p)
			for r in rels:
				providers.append(r.provider)
			practice_providers[p] = providers
		return render(request, 'feeds/view_feed.html', {'practice_providers' : practice_providers, 'feed': f})
	return new(request)

def delete_feed(request):
	if request.method == 'POST':
		f = feed.objects.get(name=request.POST['original_name'])
		f.delete()
	return new(request)

def delete_member(request):
	if request.method == 'POST':
		mem = member.objects.get(ssn=request.POST['original_name'])
		mem.delete()
	return new(request)

def delete_practice(request):
	if request.method == 'POST':
		p = practice.objects.get(name=request.POST['original_name'])
		p.delete()
	return new(request)

def delete_provider(request):
	if request.method == 'POST':
		p = provider.objects.get(identifier=request.POST['original_name'])
		p.delete()
	return new(request)

def download_rels(request):
	f = feed.objects.get(pk=request.POST['feed'])
	today = str(datetime.datetime.today().year) + str(datetime.datetime.today().month) + str(datetime.datetime.today().day)
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=nalari_' + today + '_provider_groups_provider.csv'
	writer = csv.writer(response, csv.excel, quoting=csv.QUOTE_ALL)
	response.write(u'\ufeff'.encode('utf8'))
	practices = practice.objects.filter(feed=f)
	for p in practices:
		rels = provider_practice_rel.objects.filter(practice=p)
		for r in rels:
			writer.writerow([r.practice.name, r.provider.source_id, r.practice_manager, r.inactive])
	return response

def download_practices(request):
	f = feed.objects.get(pk=request.POST['feed'])
	today = str(datetime.datetime.today().year) + str(datetime.datetime.today().month) + str(datetime.datetime.today().day)
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=nalari_' + today + '_provider_group.csv'
	writer = csv.writer(response, csv.excel, quoting=csv.QUOTE_ALL)
	response.write(u'\ufeff'.encode('utf8'))
	practices = practice.objects.filter(feed=f)
	for p in practices:
		# writer.writerow([p.source_id, p.name, p.address1, p.address2, p.city, p.state, p.phone, p.fax, p.hours, p.tax_id, p.npi, p.isolated])
		writer.writerow([p.source_id, p.name, p.address1, p.address2, p.city, p.state, p.phone, p.hours, p.tax_id, p.npi, p.isolated])
	return response

def download_providers(request):
	f = feed.objects.get(pk=request.POST['feed'])
	today = str(datetime.datetime.today().year) + str(datetime.datetime.today().month) + str(datetime.datetime.today().day)
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=nalari_' + today + '_provider.csv'
	writer = csv.writer(response, csv.excel, quoting=csv.QUOTE_ALL)
	response.write(u'\ufeff'.encode('utf8'))
	practices = practice.objects.filter(feed=f)
	for p in practices:
		rels = provider_practice_rel.objects.filter(practice=p)
		for r in rels:
			prov = r.provider 
			if prov.identifier_type == 'SSN':
				writer.writerow([prov.source_id, prov.specialty_type, "1", prov.prefix, prov.first_name, prov.middle_initial, prov.last_name, prov.gender, str(prov.dob.year) + str(prov.dob.month) + str(prov.dob.day), prov.identifier, "", "", "", "", prov.address1, prov.address2, prov.city, prov.state, prov.zipcode, prov.country, prov.phone, str(prov.start_date.year) + str(prov.start_date.month) + str(prov.start_date.day), "99990101", "1", "1", "", "1", prov.username, prov.password, "1", "1", "", "2", "", "", "", "2", "1"])
			elif prov.identifier_type == 'EIN':
				writer.writerow([prov.source_id, prov.specialty_type, "1", prov.prefix, prov.first_name, prov.middle_initial, prov.last_name, prov.gender, str(prov.dob.year) + str(prov.dob.month) + str(prov.dob.day), "", prov.identifier, "", "", "", prov.address1, prov.address2, prov.city, prov.state, prov.zipcode, prov.country, prov.phone, str(prov.start_date.year) + str(prov.start_date.month) + str(prov.start_date.day), "99990101", "1", "1", "", "1", prov.username, prov.password, "1", "1", "", "2", "", "", "", "2", "1"])
			elif prov.identifier_type == 'UPIN':
				writer.writerow([prov.source_id, prov.specialty_type, "1", prov.prefix, prov.first_name, prov.middle_initial, prov.last_name, prov.gender, str(prov.dob.year) + str(prov.dob.month) + str(prov.dob.day), "", "", prov.identifier, "", "", prov.address1, prov.address2, prov.city, prov.state, prov.zipcode, prov.country, prov.phone, str(prov.start_date.year) + str(prov.start_date.month) + str(prov.start_date.day), "99990101", "1", "1", "", "1", prov.username, prov.password, "1", "1", "", "2", "", "", "", "2", "1"])
			elif prov.identifier_type == 'NPI':
				writer.writerow([prov.source_id, prov.specialty_type, "1", prov.prefix, prov.first_name, prov.middle_initial, prov.last_name, prov.gender, str(prov.dob.year) + str(prov.dob.month) + str(prov.dob.day), "", "", "", prov.identifier, "", prov.address1, prov.address2, prov.city, prov.state, prov.zipcode, prov.country, prov.phone, str(prov.start_date.year) + str(prov.start_date.month) + str(prov.start_date.day), "99990101", "1", "1", "", "1", prov.username, prov.password, "1", "1", "", "2", "", "", "", "2", "1"])
			else: 
				writer.writerow([prov.source_id, prov.specialty_type, "1", prov.prefix, prov.first_name, prov.middle_initial, prov.last_name, prov.gender, str(prov.dob.year) + str(prov.dob.month) + str(prov.dob.day), "", "", "", "", prov.identifier, prov.address1, prov.address2, prov.city, prov.state, prov.zipcode, prov.country, prov.phone, str(prov.start_date.year) + str(prov.start_date.month) + str(prov.start_date.day), "99990101", "1", "1", "", "1", prov.username, prov.password, "1", "1", "", "2", "", "", "", "2", "1"])
	return response