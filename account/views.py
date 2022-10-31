from django.shortcuts import render,redirect
from .models import MyUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
import random
from django.contrib.auth.hashers import make_password
from django.contrib import messages
# Create your views here.
def RegsierView(request):
	return render(request,'account/register.html',{})


def send_sms_test(request):
    number = random.randint(1000, 9999)
    print(number)
    if request.method == "POST":
        phone = request.POST.get('phone')
        if MyUser.objects.filter(phone=phone):
            MyUser.objects.filter(phone=phone).update(token=number)
        else:
            MyUser.objects.create(username=phone,phone=phone,token=number)
            
    # api = KavenegarAPI('4D526E3432522F42744D47414B3845436D59734377572B71645A455565644575')
    # params = { 'sender' : '10000080808880', 'receptor': f'{phone}', 'message' :f'{number}' }
    # api.sms_send( params)
        response = render(request,'account/verify.html')
        x = phone
        response.set_cookie('phone_number_cookie',x,1000)
        return response



def VerifyChecked(request):
    if request.method == "POST":
        token = request.POST.get('token')
        phone_c = request.COOKIES['phone_number_cookie']
        try :
            user = MyUser.objects.get(phone= phone_c)
        except:
            messages.error(request,'شما اکانتی با این شماره ندارید')
        if user.token == token :
            MyUser.objects.filter(phone=phone_c).update(is_verify=True)
            return render(request,'account/complateprofile.html',{})
        else :
            messages.error(request,'کدارسالی را درست وارد کنید')
        return redirect('/')


def ComplateProfile(request):
	if request.method == "POST":
		# username=request.POST.get('username')
		password = request.POST.get('password')
		phone_c = request.COOKIES['phone_number_cookie']
		MyUser.objects.filter(phone=phone_c).update(
			username=phone_c,password=make_password(password)
		)
		messages.success(request,'پروفایل شما با موفقیت ساخته شد')
		user = MyUser.objects.get(username=phone_c)
		login(request, user)
		return redirect('/')
	else:
		return render(request,'account/complateprofile.html',{})


def respass(request):
    return render(request,'account/eghdam.html')


def SendSmsReset(request):
    number = random.randint(1000, 9999)
    print(number)
    if request.method == "POST":
        phone = request.POST.get('phone')
        if MyUser.objects.filter(phone=phone):
            MyUser.objects.filter(phone=phone).update(token=number)
        else:
            messages.error(request,'شما هیج اکانتی ندارید ابتدا برای خود حساب بسازید')
            return redirect('/register')
    # api = KavenegarAPI('4D526E3432522F42744D47414B3845436D59734377572B71645A455565644575')
    # params = {'sender' : '10000080808880', 'receptor': f'{phone}', 'message' :f'{number}' }
    # api.sms_send( params)
    response = render(request,'account/verify2.html')
    x =phone
    response.set_cookie('phone_number_cookie',x,1000)
    return response 


def ResetProfileView(request):
    return render(request,'account/ResetPasswordView.html',{})


def ResetProfile(request):
    if request.method == "POST":
        # username=request.POST.get('username')
        password = request.POST.get('password')
        phone_c = request.COOKIES['phone_number_cookie']
        MyUser.objects.filter(phone=phone_c).update(
            password=make_password(password)
        )
        messages.success(request,'عملیات با موفقیت انجام شد')
    return redirect('/')


def VerifyChecked2(request):
    if request.method == "POST":
        token = request.POST.get('token')
        phone_c = request.COOKIES['phone_number_cookie']
        try :
            user = MyUser.objects.get(phone= phone_c)
        except:
            messages.error(request,'شما اکانتی با این شماره ندارید')

        if user.token == token :
            return render(request,'account/ResetPasswordView.html')
        else:
            messages.error(request,'!!! کدارسالی را درست وارد کنید')
        return redirect('/')

def LoginView(request):
	if request.method == "POST":
		form = AuthenticationForm(data=request.POST)
		print("mas")
		if form.is_valid():
			user = form.get_user()
			if user.is_verify:
				login(request, user)
			else:
				messages.error(request,"شما احراز هویت نشده ایید")
			return redirect("/")

	form = AuthenticationForm()
	return render(request,'account/login.html',{'form':form})


