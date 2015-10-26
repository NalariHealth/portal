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

SPECIALTY_CHOICES = (
	(128, 'Nurse Midwife'),
	(129, 'Nurse Practictioner'),
	(130, 'OBGYN'),
	(131, 'Occupational Therapist'),
	(132, 'Oncologist'),
	(133, 'Optometrist'),
	(134, 'Ophthalmologist'),
	(135, 'Oral Surgeon'),
	(136, 'Orthopedist'),
	(137, 'Otolaryngologist'),
	(138, 'Pathologist'),
	(139, 'Pediatrician'),
	(140, 'Peer Mentor'),
	(141, 'Podiatrist'),
	(142, 'Physical Therapist'),
	(143, 'Physician\'s Assistant'),
	(144, 'Psychiatrist'),
	(145, 'Psychiatric Clinical Nurse Specialist'),
	(146, 'Psychologist'),
	(147, 'Pulmonologist'),
	(148, 'Radiologist'),
	(149, 'Rheumatologist'),
	(150, 'Sleep Therapist'),
	(151, 'Social Worker'),
	(152, 'Urologist'),
	(153, 'Vascular Surgeon'),
	(154, 'Trauma Surgeon'),
	(155, 'Emergency Physician'),
	(156, 'Emergency Triage'),
	(157, 'Hospitalist'),
	(158, 'Geriatrician'),
	(159, 'Geriatric Psychiatrist'),
	(160, 'Speech-Language Therapist'),
	(161, 'Orthopedic Surgeon'),
	(162, 'Care Coordinator'),
	(163, 'Nurse Care Coordinator'),
	(164, 'Medical Technician'),
	(165, 'Peer Counselor'),
	(166, 'Geriatric Fellow'),
	(100, 'Allergist'),
	(101, 'Anesthesiologist'),
	(102, 'Advanced Practice Registered Nurse'),
	(103, 'Behavioral Health Provider'),
	(104, 'Cardiologist'),
	(105, 'Child Care Nurse'),
	(106, 'Clinical Nurse Specialist'),
	(107, 'Cosmetic Surgeon'),
	(108, 'Dentist'),
	(109, 'Dermatologist'),
	(110, 'Dietician'),
	(111, 'Direct Service Support'),
	(112, 'Endocrinologist'),
	(113, 'Family Caregiver'),
	(114, 'Fitness Coach'),
	(115, 'Gastroenterologist'),
	(116, 'General Surgeon'),
	(117, 'Geriatric Psychologist'),
	(118, 'Home Health Aid'),
	(119, 'Health Coach'),
	(120, 'Hematology'),
	(121, 'Immunology'),
	(122, 'Infectious Diseases Specialist'),
	(123, 'Internist'),
	(124, 'Nephrologist'),
	(125, 'Neurologist'),
	(126, 'Nurse'),
	(127, 'Nurse Case Manager'),
)

class feed(models.Model):
	name = models.CharField(max_length=300, unique=True)
	def __str__(self):
		return self.name
	def create_downloadable_csv(username):
		return None 

class practice(models.Model):
	feed = models.ForeignKey(feed)
	source_id = models.CharField(max_length=50, verbose_name="Source ID")
	name = models.CharField(max_length=35, unique=True)
	address1 = models.CharField(max_length=255, verbose_name="Address Line 1")
	address2 = models.CharField(max_length=255, verbose_name="Address Line 2", null=True)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	phone = models.CharField(max_length=50)
	fax = models.CharField(max_length=50, null=True)
	hours = models.CharField(max_length=50)
	tax_id = models.CharField(max_length=50, verbose_name="Tax ID")
	npi = models.CharField(max_length=50, verbose_name="NPI")
	isolated = models.IntegerField(default=1, choices=NUMBER_CHOICES, verbose_name="Isolated?")
	def __str__(self):
		return self.name 

class provider(models.Model):
	feed = models.ForeignKey(feed)
	source_id = models.CharField(max_length=50, verbose_name="Source ID")
	specialty_type = models.IntegerField(choices=SPECIALTY_CHOICES, verbose_name="Specialty Type")
	prefix = models.CharField(max_length=10)
	first_name = models.CharField(max_length=100, verbose_name="First Name")
	middle_initial = models.CharField(max_length=1, verbose_name="Middle Initial")
	last_name = models.CharField(max_length=100, verbose_name="Last Name")
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	dob = models.DateField(verbose_name="Date of Birth")
	identifier = models.CharField(max_length=50)
	identifier_type = models.CharField(max_length=4, choices=ID_CHOICES, verbose_name="Identifier Type")
	address1 = models.CharField(max_length=255, verbose_name="Address Line 1")
	address2 = models.CharField(max_length=255, verbose_name="Address Line 2", null=True)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=2)
	zipcode = models.CharField(max_length=15)
	country = models.CharField(max_length=255)
	phone = models.CharField(max_length=50)
	start_date = models.DateField(verbose_name="Start Date")
	username = models.CharField(max_length=50, unique=True)
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
	subscriber_suffix = models.CharField(max_length=5, verbose_name="Subscriber Suffix")
	relationship_to_subscriber = models.CharField(max_length=5, verbose_name="Relationship to Subscriber")
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
	ssn = models.CharField(max_length=50, unique=True, verbose_name="Social Security Number")
	username = models.CharField(max_length=50, unique=True)
	password = models.CharField(max_length=50)
	pool_constrained = models.IntegerField(choices=NUMBER_CHOICES, verbose_name="Pool Constrained?")
	def __str__(self):
		return self.first_name + ' ' + self.last_name

