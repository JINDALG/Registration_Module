from django.db import models
import datetime
# Create your models here.

class Student(models.Model):
	name = models.CharField()
	contact = models.CharField()
	email = models.CharField()
	college = models.CharField()
	