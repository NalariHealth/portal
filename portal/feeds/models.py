from django.db import models
from django.forms import ModelForm 

GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female'),
)

NUMBER_CHOICES = (
	(1, 'True'),
	(2, 'False'),
)

ID_CHOICES = (
	('SSN', 'SSN'),
	('EIN', 'EIN'),
	('UPIN', 'UPIN'),
	('NPI', 'NPI'),
	('DEA', 'DEA'),
)

class feed(models.Model):
	name = models.CharField(max_length=300)
	def __str__(self):
		return self.name
	def create_downloadable_csv(username):
		return None 

class practice(models.Model):
	feed = models.ForeignKey(feed)
	source_id = models.CharField(max_length=50, verbose_name="Source ID")
	name = models.CharField(max_length=35)
	address1 = models.CharField(max_length=255, verbose_name="Address Line 1")
	address2 = models.CharField(max_length=255, verbose_name="Address Line 2")
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	phone = models.CharField(max_length=50)
	hours = models.CharField(max_length=50)
	tax_id = models.CharField(max_length=50, verbose_name="Tax ID")
	npi = models.CharField(max_length=50, verbose_name="NPI")
	isolated = models.IntegerField(default=1, choices=NUMBER_CHOICES, verbose_name="Isolated?")
	def __str__(self):
		return self.name 

class provider(models.Model):
	feed = models.ForeignKey(feed)
	source_id = models.CharField(max_length=50, verbose_name="Source ID")
	specialty_type = models.IntegerField(verbose_name="Specialty Type")
	prefix = models.CharField(max_length=10)
	first_name = models.CharField(max_length=100, verbose_name="First Name")
	middle_initial = models.CharField(max_length=1, verbose_name="Middle Initial")
	last_name = models.CharField(max_length=100, verbose_name="Last Name")
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	dob = models.DateField(verbose_name="Date of Birth")
	identifier = models.CharField(max_length=50)
	identifier_type = models.CharField(max_length=4, choices=ID_CHOICES, verbose_name="Identifier Type")
	address1 = models.CharField(max_length=255, verbose_name="Address Line 1")
	address2 = models.CharField(max_length=255, verbose_name="Address Line 2")
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	zipcode = models.CharField(max_length=15)
	country = models.CharField(max_length=255)
	phone = models.CharField(max_length=50)
	start_date = models.DateField(verbose_name="Start Date")
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	def __str__(self):
		return self.first_name + ' ' + self.last_name

class provider_practice_rel(models.Model):
	provider = models.ForeignKey(provider)
	practice = models.ForeignKey(practice)
	inactive = models.IntegerField(default=2, choices=NUMBER_CHOICES, verbose_name="Inactive?")
	practice_manager = models.IntegerField(default=1, choices=NUMBER_CHOICES, verbose_name="Practice Manager?")
	def __str__(self):
		return str(provider) + '!@#' + str(practice)

class member(models.Model):
	member_source_id = models.CharField(max_length=50, verbose_name="Member Source ID")
	subscriber_id = models.CharField(max_length=50, verbose_name="Subscriber ID")
	group_id = models.ForeignKey(practice, verbose_name="Group ID")
	first_name = models.CharField(max_length=100, verbose_name="First Name")
	middle_initial = models.CharField(max_length=1, verbose_name="Middle Initial")
	last_name = models.CharField(max_length=100, verbose_name="Last Name")
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	dob = models.DateField(verbose_name="Date of Birth")
	address1 = models.CharField(max_length=255, verbose_name="Address Line 1")
	address2 = models.CharField(max_length=255, verbose_name="Address Line 2")
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	zipcode = models.CharField(max_length=15)
	country = models.CharField(max_length=255)
	phone = models.CharField(max_length=50)
	secondary_phone = models.CharField(max_length=50, verbose_name="Secondary Phone")
	email_address = models.CharField(max_length=50, verbose_name="Email Address")
	start_date = models.DateField(verbose_name="Start Date")
	ssn = models.CharField(max_length=50, verbose_name="Social Security Number")
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	pool_constrained = models.IntegerField(choices=NUMBER_CHOICES, verbose_name="Pool Constrained?")
	def __str__(self):
		return self.first_name + ' ' + self.last_name

