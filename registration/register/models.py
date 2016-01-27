from django.db import models
import datetime
from django.core.validators import RegexValidator
# Create your models here.

class Student(models.Model):

	course_choice = (
		('btech','B.Tech'),
		('mtech','M.Tech'),
		('mba','MBA & MAM'),
		('mca','MCA'),
		)
	branch_choice = (
		('cs','CS'),
		('it','IT'),
		('me','ME'),
		('eee','EEE'),
		('ic','IC'),
		('civil','CIVIL'),
		)

	year_choice = (
		(1,'1'),
		(2,'2'),
		(3,'3'),
		(4,'4')
		)
	phone_regx = RegexValidator(regex=r'^\d{10}$', message="Phone number must be ten digit")
	name_regx = RegexValidator(regex=r"^[a-zA-Z]{3,20}$", message="This is not a valid name")
	name = models.CharField(max_length = 20, validators = [name_regx])
	email = models.EmailField(primary_key = True)
	course = models.CharField(max_length = 20, choices = course_choice, default = 'btech' ,blank = False)
	contact = models.CharField(max_length = 20, validators = [phone_regx] )
	branch = models.CharField(max_length = 20,blank = True, choices = branch_choice)
	college = models.CharField(max_length = 20, blank = False)
	year = models.CharField(choices = year_choice, max_length = 1)

	def __unicode__(self):
		return self.name
	