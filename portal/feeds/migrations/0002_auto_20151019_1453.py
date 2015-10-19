# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address1',
            field=models.CharField(max_length=255, verbose_name=b'Address Line 1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='address2',
            field=models.CharField(max_length=255, verbose_name=b'Address Line 2'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='dob',
            field=models.DateField(verbose_name=b'Date of Birth'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='email_address',
            field=models.CharField(max_length=50, verbose_name=b'Email Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name=b'First Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='group_id',
            field=models.ForeignKey(verbose_name=b'Group ID', to='feeds.practice'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name=b'Last Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='member_source_id',
            field=models.CharField(max_length=50, verbose_name=b'Member Source ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='middle_initial',
            field=models.CharField(max_length=1, verbose_name=b'Middle Initial'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='pool_constrained',
            field=models.IntegerField(verbose_name=b'Pool Constrained?', choices=[(1, b'True'), (2, b'False')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='secondary_phone',
            field=models.CharField(max_length=50, verbose_name=b'Secondary Phone'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='ssn',
            field=models.CharField(max_length=50, verbose_name=b'Social Security Number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='start_date',
            field=models.DateField(verbose_name=b'Start Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='subscriber_id',
            field=models.CharField(max_length=50, verbose_name=b'Subscriber ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practice',
            name='address1',
            field=models.CharField(max_length=255, verbose_name=b'Address Line 1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practice',
            name='address2',
            field=models.CharField(max_length=255, verbose_name=b'Address Line 2'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practice',
            name='isolated',
            field=models.IntegerField(default=1, verbose_name=b'Isolated?', choices=[(1, b'True'), (2, b'False')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practice',
            name='npi',
            field=models.CharField(max_length=50, verbose_name=b'NPI'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practice',
            name='source_id',
            field=models.CharField(max_length=50, verbose_name=b'Source ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='practice',
            name='tax_id',
            field=models.CharField(max_length=50, verbose_name=b'Tax ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='address1',
            field=models.CharField(max_length=255, verbose_name=b'Address Line 1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='address2',
            field=models.CharField(max_length=255, verbose_name=b'Address Line 2'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='dob',
            field=models.DateField(verbose_name=b'Date of Birth'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name=b'First Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='identifier_type',
            field=models.CharField(max_length=4, verbose_name=b'Identifier Type', choices=[(b'SSN', b'SSN'), (b'EIN', b'EIN'), (b'UPIN', b'UPIN'), (b'NPI', b'NPI'), (b'DEA', b'DEA')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name=b'Last Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='middle_initial',
            field=models.CharField(max_length=1, verbose_name=b'Middle Initial'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='source_id',
            field=models.CharField(max_length=50, verbose_name=b'Source ID'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='specialty_type',
            field=models.IntegerField(verbose_name=b'Specialty Type', choices=[(128, b'Nurse Midwife'), (129, b'Nurse Practictioner'), (130, b'OBGYN'), (131, b'Occupational Therapist'), (132, b'Oncologist'), (133, b'Optometrist'), (134, b'Ophthalmologist'), (135, b'Oral Surgeon'), (136, b'Orthopedist'), (137, b'Otolaryngologist'), (138, b'Pathologist'), (139, b'Pediatrician'), (140, b'Peer Mentor'), (141, b'Podiatrist'), (142, b'Physical Therapist'), (143, b"Physician's Assistant"), (144, b'Psychiatrist'), (145, b'Psychiatric Clinical Nurse Specialist'), (146, b'Psychologist'), (147, b'Pulmonologist'), (148, b'Radiologist'), (149, b'Rheumatologist'), (150, b'Sleep Therapist'), (151, b'Social Worker'), (152, b'Urologist'), (153, b'Vascular Surgeon'), (154, b'Trauma Surgeon'), (155, b'Emergency Physician'), (156, b'Emergency Triage'), (157, b'Hospitalist'), (158, b'Geriatrician'), (159, b'Geriatric Psychiatrist'), (160, b'Speech-Language Therapist'), (161, b'Orthopedic Surgeon'), (162, b'Care Coordinator'), (163, b'Nurse Care Coordinator'), (164, b'Medical Technician'), (165, b'Peer Counselor'), (166, b'Geriatric Fellow'), (100, b'Allergist'), (101, b'Anesthesiologist'), (102, b'Advanced Practice Registered Nurse'), (103, b'Behavioral Health Provider'), (104, b'Cardiologist'), (105, b'Child Care Nurse'), (106, b'Clinical Nurse Specialist'), (107, b'Cosmetic Surgeon'), (108, b'Dentist'), (109, b'Dermatologist'), (110, b'Dietician'), (111, b'Direct Service Support'), (112, b'Endocrinologist'), (113, b'Family Caregiver'), (114, b'Fitness Coach'), (115, b'Gastroenterologist'), (116, b'General Surgeon'), (117, b'Geriatric Psychologist'), (118, b'Home Health Aid'), (119, b'Health Coach'), (120, b'Hematology'), (121, b'Immunology'), (122, b'Infectious Diseases Specialist'), (123, b'Internist'), (124, b'Nephrologist'), (125, b'Neurologist'), (126, b'Nurse'), (127, b'Nurse Case Manager')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='start_date',
            field=models.DateField(verbose_name=b'Start Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider_practice_rel',
            name='inactive',
            field=models.IntegerField(default=2, verbose_name=b'Inactive?', choices=[(1, b'True'), (2, b'False')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider_practice_rel',
            name='practice_manager',
            field=models.IntegerField(default=1, verbose_name=b'Practice Manager?', choices=[(1, b'True'), (2, b'False')]),
            preserve_default=True,
        ),
    ]
