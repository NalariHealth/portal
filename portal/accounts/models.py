from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
	user = models.ForeignKey(User, unique=True)
	zoom_id = models.CharField(max_length=70)
	MD = models.BooleanField(default=False)
	DO = models.BooleanField(default=False)
	online = models.BooleanField(default=False)
	def __str__(self):
		to_add = ''
		if self.MD:
			to_add = to_add + ', M.D.'
		if self.DO:
			to_add = to_add + ', D.O.'
		return (self.user.get_full_name() + to_add)

class Patient(models.Model):
	user = models.ForeignKey(User, unique=True)
	zoom_id = models.CharField(max_length=70)
	def __str__(self):
		return self.user.get_full_name()