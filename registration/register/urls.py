from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^register/$', views.Register.as_view(), name= 'register'),
	#url(r'^$', views.thanks.as_view(), name= 'thanks'),

]