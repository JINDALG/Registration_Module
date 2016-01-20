from django.shortcuts import render
from .models import Student
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Register
from django import forms
import re

name_RE = re.compile(r"^[a-zA-Z ]{3,20}$")
def valid_name(name):
    return name and name_RE.match(name)


mobile_re = re.compile(r"^[0-9]{10}$")
def valid_mobile(mobile):
    return mobile and mobile_re.match(mobile)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

def valid_college(college):
	if college == 'JSSATEN' or college == 'others':
		return True
	return False


def register(request):
	if request.method == 'POST':
		form = Register(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			course = form.cleaned_data['course']
			contact = form.cleaned_data['contact']
			college = form.cleaned_data['college']
			year = form.cleaned_data['year']
			have_error = False
			params = dict(name = name,email = email,contact = contact , form = Register())
			if not valid_name(name):
				params['error_name'] = 'Enter a valid name'
				have_error = True
			if not valid_mobile(contact):
				params['error_contact'] = 'contact number must be 10 digits'
				have_error = True
			if not valid_email(email):
				params['error_email'] = 'Enter a valid email id'
				have_error = True
			if not valid_college(college):
				params['error_college'] = 'Enetr a valid college name'
				have_error = True
			if year >4 or year < 1 :
				params['error_year'] = 'Enter current college year'
				have_error == True
			if not (course == 'B.tech' or course=='M.tech' or course=='MCA' or course=='MBA'):
				params['error_course'] = 'Enter your college course'
				have_error = True

			student = Student.objects.filter(email = email)
			if student:
				params['error_email'] = 'Student already registered.'
				have_error = True
			if have_error:
				return render(request , 'register/register.html' , params)
			else :
				user = Student(name = name, email = email, course = course, contact = contact, college = college, year = year)
				user.save()
				return HttpResponseRedirect('/registration')

		else :
			errors = form.errors
			errors = errors.values()
			error = errors[0]
			form = Register()
			return render(request,'register/register.html',{'form':form , 'error':error})

	else :
		form = Register()
		return render(request,'register/register.html',{'form':form})


def thanks(request):
	return HttpResponse('You are Registered.')