from django.shortcuts import render
from django.forms import ModelForm, Form, ModelChoiceField
from models import feed, practice, provider, provider_practice_rel, member 
from django.core.exceptions import MultipleObjectsReturned
from django import forms

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
	practice = ModelChoiceField(queryset=practice.objects.all(), widget=forms.Select(attrs={"onChange": 'submit();'}), label='Provider/Practice Relationship')

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
			form.save()
			return new(request)
	form = feedForm()
	return render(request, 'feeds/new_feed.html', {'form': form})

def new_practice(request):
	if request.method == 'POST':
		form = practiceForm(request.POST)
		if form.is_valid():
			nf = form.save()
			request.method = 'GET'
			return new(request)
	form = practiceForm()
	return render(request, 'feeds/new_practice.html', {'form': form})

def new_provider(request):
	if request.method == 'POST':
		form = providerForm(request.POST)
		if form.is_valid():
			nf = form.save()
			request.method = 'GET'
			return new(request)
	form = providerForm()
	return render(request, 'feeds/new_provider.html', {'form': form})

def new_member(request):
	if request.method == 'POST':
		form = memberForm(request.POST)
		if form.is_valid():
			nf = form.save()
			request.method = 'GET'
			return new(request)
	form = memberForm()
	return render(request, 'feeds/new_member.html', {'form': form})

def new_pprel(request):
	if request.method == 'POST':
		form = pprelForm(request.POST)
		if form.is_valid():
			nf = form.save()
			try:
				existing = provider_practice_rel.objects.get(provider=nf.provider, practice=nf.practice)
			except MultipleObjectsReturned:
				nf.delete()
			return new(request)
	form = pprelForm()
	return render(request, 'feeds/new_pprel.html', {'form': form})

def select_feed(request):
	if request.method == 'POST':
		f = feed.objects.get(pk=request.POST['feed'])
		original_name = f.name 
		form = feedForm(instance=f)
		return render(request, 'feeds/edit_feed.html', {'form': form, 'instance': original_name})
	else:
		return new(request)

def edit_feed(request):
	if request.method == 'POST':
		original_name = request.POST['original_name']
		original_feed = feed.objects.get(name=original_name)
		form = feedForm(request.POST, instance=original_feed)
		if form.is_valid():
			form.save()
	return new(request)

def select_practice(request):
	if request.method == 'POST':
		p = practice.objects.get(pk=request.POST['practice'])
		original_name = p.name 
		form = practiceForm(instance=p)
		return render(request, 'feeds/edit_practice.html', {'form': form, 'instance': original_name})
	else:
		return new(request)

def edit_practice(request):
	if request.method == 'POST':
		original_name = request.POST['original_name']
		original_practice = practice.objects.get(name=original_name)
		form = practiceForm(request.POST, instance=original_practice)
		if form.is_valid():
			form.save()
	return new(request)

def select_provider(request):
	if request.method == 'POST':
		p = provider.objects.get(pk=request.POST['provider'])
		original_id = p.identifier 
		form = providerForm(instance=p)
		return render(request, 'feeds/edit_provider.html', {'form': form, 'instance': original_id})
	else:
		return new(request)

def edit_provider(request):
	if request.method == 'POST':
		original_id = request.POST['original_name']
		original_provider = provider.objects.get(identifier=original_id)
		form = providerForm(request.POST, instance=original_provider)
		if form.is_valid():
			form.save()
	return new(request)

def select_member(request):
	if request.method == 'POST':
		m = member.objects.get(pk=request.POST['member'])
		original_id = m.ssn
		form = memberForm(instance=m)
		return render(request, 'feeds/edit_member.html', {'form': form, 'instance': original_id})
	else:
		return new(request)

def edit_member(request):
	if request.method == 'POST':
		original_id = request.POST['original_name']
		original_member = member.objects.get(ssn=original_id)
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
		original_id = r.id
		form = pprelForm(instance=r)
		return render(request, 'feeds/edit_rel.html', {'form': form, 'instance': original_id})
	return new(request)

def edit_rel(request):
	if request.method == 'POST':
		original_id = request.POST['original_name']
		original_rel = provider_practice_rel.objects.get(pk=original_id)
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