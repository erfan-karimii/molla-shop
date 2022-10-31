from django.urls import path
from . import views

app_name='contactus'


urlpatterns = [
	path('khabarname/',views.khabar_name,name='khabar_name'),
	path('contactus/',views.contact_us,name='contact_us'),
]