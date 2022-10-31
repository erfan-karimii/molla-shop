from django.shortcuts import render , redirect
from django.contrib import messages
from .models import ContactUs, KhabarName , OurShop , ContactDetail
from .forms import KhabarNameForm , ContactUsForm

# Create your views here.

def khabar_name(request):
    if request.method == 'POST':
        print(request.POST)
        form = KhabarNameForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # duplicate with validation should be check
            KhabarName.objects.create(email=email)
            messages.success(request, 'ایمیل شما با موفقیت ثبت شد.')
            return redirect('home:home')
        else:
            print(form.errors)
            if 'Enter a valid email address' in str(form.errors):                
                messages.error(request, 'ظاهرا مشکلی پیش امده است لطفا دوباره امتحان کنید.')
            elif 'duplicate email' in str(form.errors):
                messages.error(request, 'این ایمیل قبلا ثبت شده است')
            return redirect('home:home')
    else:
        print('what?')
        return redirect('home:home')

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            email = request.POST.get('email')
            ContactUs.objects.create(name=name,email=email,phone=phone,title=title,body=body)
            messages.success(request,'.پیام شما با موفقیت دریافت شد')
        else:
            print(form.errors,'testtt')
            messages.error(request,'.متاسفانه مشکلی رخ داده است لطفا دوباره تلاش کنید')
    context = {
        'ourshops' : OurShop.objects.all(),
        'contact' : ContactDetail.objects.first(),
    }
    return render(request,'contact.html',context)