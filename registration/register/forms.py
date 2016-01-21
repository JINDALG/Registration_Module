from django import forms

class Register(forms.Form):
	name = forms.CharField(label='name' , max_length = 20);
	email   = forms.EmailField(label='email')
	course  = forms.ChoiceField(choices =(('B.Tech','B.Tech'),('MBA','MBA'),('MCA','MCA'),('M.Tech','M.Tech')))
	contact = forms.CharField(label='contact')
	college = forms.ChoiceField(choices =(('jssaten','jssaten'),('others','others')))
	othercollege = forms.CharField(required=False)
	year    = forms.ChoiceField(choices =((1,'1'),(2,'2'),(3,'3'),(4,'4')))