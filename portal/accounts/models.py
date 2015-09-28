from django.db import models
from django.contrib.auth.models import User

## SETTINGS ## 
class tile_option(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	a_interior = models.CharField(max_length=300)
	def __str__(self):
		return self.title

class list_option(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=20)
	a_interior = models.CharField(max_length=300)
	def __str__(self):
		return self.title

class settings(models.Model):
	id = models.AutoField(primary_key=True)
	tile_1 = models.ForeignKey(tile_option, null=True, related_name='tile_1', on_delete=models.SET_NULL)
	tile_2 = models.ForeignKey(tile_option, null=True, related_name='tile_2', on_delete=models.SET_NULL)
	tile_3 = models.ForeignKey(tile_option, null=True, related_name='tile_3', on_delete=models.SET_NULL)
	tile_4 = models.ForeignKey(tile_option, null=True, related_name='tile_4', on_delete=models.SET_NULL)
	tile_5 = models.ForeignKey(tile_option, null=True, related_name='tile_5', on_delete=models.SET_NULL)
	tile_6 = models.ForeignKey(tile_option, null=True, related_name='tile_6', on_delete=models.SET_NULL)
	list_option_1 = models.ForeignKey(list_option, null=True, related_name='list_option_1', on_delete=models.SET_NULL)
	list_option_2 = models.ForeignKey(list_option, null=True, related_name='list_option_2', on_delete=models.SET_NULL)
	list_option_3 = models.ForeignKey(list_option, null=True, related_name='list_option_3', on_delete=models.SET_NULL)
	list_option_4 = models.ForeignKey(list_option, null=True, related_name='list_option_4', on_delete=models.SET_NULL)
	list_option_5 = models.ForeignKey(list_option, null=True, related_name='list_option_5', on_delete=models.SET_NULL)
	list_option_6 = models.ForeignKey(list_option, null=True, related_name='list_option_6', on_delete=models.SET_NULL)
	def __str__(self):
		tiles = [self.tile_1, self.tile_2, self.tile_3, self.tile_4, self.tile_5, self.tile_6]
		lists = [self.list_option_1, self.list_option_2, self.list_option_3, self.list_option_4, self.list_option_5, self.list_option_6]
		return ' '.join(tiles) + '\n' + ' '.join(lists)

## USERS ##
class picture(models.Model):
	picfile = models.FileField(upload_to='user_photos')


class gen_user(models.Model):
	user = models.ForeignKey(User, unique=True)
	settings = models.ForeignKey(settings, default=1)
	picture = models.ForeignKey(picture, null=True)
	def __str__(self):
		return self.user.get_full_name()

class Doctor(models.Model):
	gen_user = models.ForeignKey(gen_user)
	# zoom_id = models.CharField(max_length=70)
	MD = models.BooleanField(default=False)
	DO = models.BooleanField(default=False)
	online = models.BooleanField(default=False)
	def __str__(self):
		to_add = ''
		if self.MD:
			to_add = to_add + ', M.D.'
		if self.DO:
			to_add = to_add + ', D.O.'
		return self.gen_user.user.get_full_name() + to_add

class Patient(models.Model):
	gen_user = models.ForeignKey(gen_user)
	# zoom_id = models.CharField(max_length=70)
	def __str__(self):
		return self.gen_user

class Caregiver(models.Model): 
	gen_user = models.ForeignKey(gen_user)
	def __str__(self):
		return self.gen_user

## USER RELATIONSHIPS ## 
class c_p_rel(models.Model):
	id = models.AutoField(primary_key=True)
	caregiver = models.ForeignKey(Caregiver)
	patient = models.ForeignKey(Patient)
	def __str__(self):
		return 'Patient: ' + str(patient) +' / Caregiver: ' + str(caregiver)