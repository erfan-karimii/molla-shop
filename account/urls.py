from django.urls import path

from . import views

app_name='account'


urlpatterns = [
	path('login/',views.LoginView,name='LoginView'),
	path('register/',views.RegsierView,name='RegsierView'),
	path('sendsms1/',views.send_sms_test,name='send'),
	path('VerifyChecked/',views.VerifyChecked,name='verify'),
	path('ComplateProfile/',views.ComplateProfile,name='comp'),
	path('resetpassword/',views.respass,name='resetpasswordsms'),
	path('sendsms2/',views.SendSmsReset,name='send2'),
	path('Changepassword2/',views.ResetProfile,name='resetprofile'),
	path('Change/',views.VerifyChecked2,name='changepass'),
]