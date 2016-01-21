from django import forms

class Register(forms.Form):
	name = forms.CharField(label='name' , max_length = 20);
	email   = forms.EmailField(label='email')
	course  = forms.CharField(label='course' ,max_length = 20)
	contact = forms.CharField(label='contact', max_length = 10)
	college = forms.ChoiceField(choices =(('jssaten','jssaten'),('others','others')))
	year    = forms.ChoiceField(choices =((1,1),(2,'2')))