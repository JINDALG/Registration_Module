from django.db import models
import datetime
# Create your models here.

class Student(models.Model):
	name = models.CharField(max_length = 20)
	email = models.EmailField()
	course = models.CharField(max_length = 20)
	contact = models.CharField(max_length = 20)
	college = models.CharField(max_length = 20)
	year = models.IntegerField()

	def __unicode__(self):
		return self.name
	