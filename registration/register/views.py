from django.shortcuts import render
from .models import Student
from django.http import HttpResponse,HttpResponseRedirect
from .forms import Register_form
from django import forms
from django.views.generic import View

def valid_college(college):
	if college != '':
		return True
	return False


class Register(View):
	form = Register_form
	template_name = 'register/register1.html'

	def get(self, request):
		return render(request, self.template_name , {'form' : self.form()})

	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid() : 
			college = request.POST.get('college')
			print college
			return render(request, self.template_name , {'form' : self.form()})

		else :
			return render(request, self.template_name , {'form' : form})






# def register(request):
# 	if request.method == 'POST':
# 		form = Register(request.POST)
# 		if form.is_valid():
# 			name = form.cleaned_data['name']
# 			email = form.cleaned_data['email']
# 			course = form.cleaned_data['course']
# 			contact = form.cleaned_data['contact']
# 			college = form.cleaned_data['college']
# 			year = form.cleaned_data['year']
# 			have_error = False
# 			params = dict(name = name,email = email,contact = contact , form = form, course = course, college = college, year = year)
# 			student = Student.objects.filter(email = email)
# 			if student:
# 				params['error_email'] = 'Student already registered.'
# 				have_error = True
# 				return render(request , 'register/register1.html' , params)
# 			if not valid_name(name):
# 				params['error_name'] = 'Enter a valid name'
# 				have_error = True
# 			if college == 'others':
# 				college = form.cleaned_data['othercollege']
# 				if not valid_college(college):
# 					params['error_college'] = "college name can't be empty"
# 					params['college'] = college
# 					have_error = True

# 			if have_error:
# 				return render(request , 'register/register1.html' , params)
# 			else :
# 				user = Student(name = name, email = email, course = course, contact = contact, college = college, year = year)
# 				user.save()
# 				return HttpResponseRedirect('/registration')

# 		else :
# 			errors = form.errors
# 			errors = errors.values()
# 			error = errors[0]
# 			return render(request,'register/register1.html',{'form':form , 'error':error})

# 	else :
# 		form = Register()	
# 		return render(request,'register/register1.html',{'form':form})


# def thanks(request):
# 	return HttpResponse('You are Registered.')