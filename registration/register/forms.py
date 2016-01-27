from django import forms
from .models import Student


class Register_form(forms.ModelForm):
	college_choice = (
		('jss', 'JSS Academy of Technical Education, Noida'),
		('others', 'OTHERS')
		)
	college = forms.ChoiceField(choices = college_choice, initial = 'jss')
	other_college = forms.CharField(required = False)
	class Meta:
		model = Student
		fields = ['name','email','course','branch','contact','college','other_college','year']