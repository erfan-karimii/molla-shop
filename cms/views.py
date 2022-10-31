from django.shortcuts import render, redirect, get_object_or_404 
from django.http import JsonResponse , HttpResponse 
from django.contrib import messages
from django.contrib.auth.hashers import make_password
import datetime
from django.db.models import ProtectedError


from aboutus.forms import FirstForm, ThreeForm, TeamForm, CompanyForm
from aboutus.models import First, Three, Team, Company

from contactus.forms import OurShopForm, KhabarNameForm, ContactUsDetailForm, ContactUsForm
from contactus.models import OurShop, KhabarName, ContactDetail, ContactUs

from account.forms import UserForm, UserCreateForm
from account.models import MyUser

from home.forms import FooterAsliForm, FooterZirForm, NavOneForm, NavTwoForm, NavThreeForm, SiteSettingForm, SliderForm, TablighForm, Tag_navbr_form, tag_footer_forms, TagNewPageForm, ZirSliderForm, FooterZirUpdateForm
from home.models import FooterAsli, FooterZir, NavOne, NavTwo, NavThree, SiteSetting, Slider, Tabligh, TagNav, TagFooter, TagNewPage, ZirSlider

from product.forms import CategoryForm, ColorForm , ZirCategoryForm , TagsForm , ProductForm , SizeForm , ColorForm , GalleryImageForm , CommentFormCMS
from product.models import Category , Size , ZirCategory , Tags , Product , Color , GalleryImage , Comment
# START --------- First -----------------------------------

def first_edit(request):
    x = First.objects.all().first()
    if request.method == "POST":
        form = FirstForm(request.POST, request.FILES, instance=x)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
        else:
            pass
    else:
        form = FirstForm(instance=x)
    context = {
        'form': form, 'x': x
    }
    return render(request, 'cms/first_edit.html', context)

# END --------- First -----------------------------------

# START ---------Three-----------------------------------

def three_view(request):
    if request.method == 'POST':
        form = ThreeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'قسمت توضیح اضافه شد ')
            return redirect('cms:three_list')
        else:
            messages.error(
                request, 'مشکلی پیش امده است لطفا دوباره تلاش کنید.')
            return redirect('cms:three_list')
    else:
        form = ThreeForm()
    context = {
        'form': form
    }
    return render(request, 'cms/three/three_view.html', context)

def list_three(request):
    threes = Three.objects.all()
    context = {
        'threes': threes,
    }
    return render(request, 'cms/three/three_list.html', context)

def detail_three_asli(request, id):
    three = get_object_or_404(Three, id=id)
    if request.method == 'POST':
        form = ThreeForm(request.POST, instance=three)
        if form.is_valid():
            form.save()
            messages.success(request, 'توضیح تغییر پیدا کرد ')
            return redirect('cms:three_list')
        else:
            messages.error(
                request, 'مشکلی پیش امده است لطفا دوباره تلاش کنید.')
            return redirect('cms:three_list')
    else:
        form = ThreeForm(instance=three)
    context = {
        'three': three,
        'form': form
    }
    return render(request, 'cms/three/three_detail.html', context)

def three_asli(request, id):
    three = get_object_or_404(Three, id=id)
    three.delete()
    messages.success(request, ' توضیح حذف شد ')
    return redirect('cms:three_list')

# END ---------Three-----------------------------------

# START ---------Team-----------------------------------

def team_view(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'یک عضو اضافه شد ')
            return redirect('cms:team_list')
        else:
            print(form.errors)
            messages.error(request, 'مشکلی پیش امده است لطفا دوباره تلاش کنید.')
            return redirect('cms:team_list')
    else:
        form = TeamForm()
    context = {
        'form': form
    }
    return render(request, 'cms/team/team_view.html', context)

def list_team(request):
    teams = Team.objects.all()
    context = {
        'teams': teams,
    }
    return render(request, 'cms/team/team_list.html', context)

def detail_team_asli(request, id):
    team = get_object_or_404(Team, id=id)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            messages.success(request, 'مشخصات عضو تغییر پیدا کرد ')
            return redirect('cms:team_list')
        else:
            messages.error(
                request, 'مشکلی پیش امده است لطفا دوباره تلاش کنید.')
            return redirect('cms:team_list')
    else:
        form = TeamForm(instance=team)
    context = {
        'team': team,
        'form': form
    }
    return render(request, 'cms/team/team_detail.html', context)

def team_asli(request, id):
    team = get_object_or_404(Team, id=id)
    team.delete()
    messages.success(request, ' عضو حذف شد ')
    return redirect('cms:team_list')

# END ---------Team-----------------------------------

# START ---------Company-----------------------------------

def company_view(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'یک کمپانی اضافه شد ')
            return redirect('cms:company_list')
        else:
            print(form.errors)
            messages.error(
                request, 'مشکلی پیش امده است لطفا دوباره تلاش کنید.')
            return redirect('cms:company_list')
    else:
        form = CompanyForm()
    context = {
        'form': form
    }
    return render(request, 'cms/company/company_view.html', context)

def list_company(request):
    companys = Company.objects.all()
    context = {
        'companys': companys,
    }
    return render(request, 'cms/company/company_list.html', context)

def detail_company_asli(request, id):
    company = get_object_or_404(Company, id=id)
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'مشخصات کمپانی تغییر پیدا کرد ')
            return redirect('cms:company_list')
        else:
            messages.error(
                request, 'مشکلی پیش امده است لطفا دوباره تلاش کنید.')
            return redirect('cms:company_list')
    else:
        form = CompanyForm(instance=company)
    context = {
        'company': company,
        'form': form
    }
    return render(request, 'cms/company/company_detail.html', context)

def company_asli(request, id):
    company = get_object_or_404(Company, id=id)
    company.delete()
    messages.success(request, ' کمپانی حذف شد ')
    return redirect('cms:company_list')

# END ---------Company-----------------------------------

# START ---------OurShop-----------------------------------

def ourshop_view(request):
    if request.method == 'POST':
        form = OurShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'یک فروشگاه اضافه شد ')
            return redirect('cms:ourshop_list')
        else:
            print(form.errors)
            messages.error(
                request, 'مشکلی پیش امده است لطفا دوباره تلاش کنید.')
            return redirect('cms:ourshop_list')
    else:
        form = OurShopForm()
    context = {
        'form': form
    }
    return render(request, 'cms/ourshop/ourshop_view.html', context)

def list_ourshop(request):
    ourshops = OurShop.objects.all()
    context = {
        'ourshops': ourshops,
    }
    return render(request, 'cms/ourshop/ourshop_list.html', context)

def detail_ourshop_asli(request, id):
    ourshop = get_object_or_404(OurShop, id=id)
    if request.method == 'POST':
        form = OurShopForm(request.POST, request.FILES, instance=ourshop)
        if form.is_valid():
            form.save()
            messages.success(request, 'مشخصات فروشگاه تغییر پیدا کرد ')
            return redirect('cms:ourshop_list')
        else:
            messages.error(
                request, 'مشکلی پیش امده است لطفا دوباره تلاش کنید.')
            return redirect('cms:ourshop_list')
    else:
        form = OurShopForm(instance=ourshop)
    context = {
        'ourshop': ourshop,
        'form': form
    }
    return render(request, 'cms/ourshop/ourshop_detail.html', context)

def ourshop_asli(request, id):
    ourshop = get_object_or_404(OurShop, id=id)
    ourshop.delete()
    messages.success(request, ' فروشگاه حذف شد ')
    return redirect('cms:ourshop_list')

# END ---------OurShop-----------------------------------

# START ---------ContactUs-----------------------------------

def list_contactus(request):
    contactuss = ContactUs.objects.all()
    context = {
        'contactuss': contactuss,
    }
    return render(request, 'cms/contactus/contactus_list.html', context)

def detail_contactus_asli(request, id):
    contactus = get_object_or_404(ContactUs, id=id)
    if request.method == 'POST':
        form = ContactUsForm(request.POST, request.FILES, instance=contactus)
        if form.is_valid():
            form.save()
            contactus.email = request.POST.get('email')
            contactus.save()
            messages.success(request, 'مشخصات فروشگاه تغییر پیدا کرد ')
            return redirect('cms:contactus_list')
        else:
            messages.error(
                request, 'مشکلی پیش امده است لطفا دوباره تلاش کنید.')
            return redirect('cms:contactus_list')
    else:
        form = ContactUsForm(instance=contactus)
    context = {
        'contactus': contactus,
        'form': form
    }
    return render(request, 'cms/contactus/contactus_detail.html', context)

def contactus_asli(request, id):
    contactus = get_object_or_404(ContactUs, id=id)
    contactus.delete()
    messages.success(request, ' فروشگاه حذف شد ')
    return redirect('cms:contactus_list')

# END ---------ContactUs-----------------------------------

# START ---------ContactUSDetail-----------------------------------

def contactusdetail_edit(request):
    x = ContactDetail.objects.all().first()
    if request.method == "POST":
        form = ContactUsDetailForm(request.POST, request.FILES, instance=x)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
        else:
            pass
    else:
        form = ContactUsDetailForm(instance=x)
    context = {
        'form': form, 'x': x
    }
    return render(request, 'cms/contactusdetail_edit.html', context)

# END ---------ContactUSDetail-----------------------------------

# START ---------KhabarName-----------------------------------

def khabarname_view(request):
    if request.method == 'POST':
        form = KhabarNameForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            KhabarName.objects.create(email=email)
            messages.success(request, 'ایمیل شما با موفقیت ثبت شد.')
            return redirect('cms:khabarname_list')
        else:
            print(form.errors)
            if 'Enter a valid email address' in str(form.errors):
                messages.error(
                    request, 'ظاهرا مشکلی پیش امده است لطفا دوباره امتحان کنید.')
            elif 'duplicate email' in str(form.errors):
                messages.error(request, 'این ایمیل قبلا ثبت شده است')
            return redirect('cms:khabarname_list')
    else:
        form = KhabarNameForm()
    context = {
        'form': form
    }
    return render(request, 'cms/khabarname/khabarname_view.html', context)

def list_khabarname(request):
    khabarnames = KhabarName.objects.all()
    context = {
        'khabarnames': khabarnames,
    }
    return render(request, 'cms/khabarname/khabarname_list.html', context)

def detail_khabarname_asli(request, id):
    khabarname = get_object_or_404(KhabarName, id=id)
    if request.method == 'POST':
        form = KhabarNameForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            KhabarName.objects.filter(
                email=khabarname.email).update(email=email)
            messages.success(request, 'ایمیل با موفقیت تغییر پیدا کرد.')
            return redirect('cms:khabarname_list')
        else:
            print(form.errors)
            if 'Enter a valid email address' in str(form.errors):
                messages.error(
                    request, 'ظاهرا مشکلی پیش امده است لطفا دوباره امتحان کنید.')
            elif 'duplicate email' in str(form.errors):
                messages.error(request, 'این ایمیل قبلا ثبت شده است')
            return redirect('cms:khabarname_list')
    else:
        form = KhabarNameForm()
    context = {
        'khabarname': khabarname,
        'form': form
    }
    return render(request, 'cms/khabarname/khabarname_detail.html', context)

def khabarname_asli(request, id):
    khabarname = get_object_or_404(KhabarName, id=id)
    khabarname.delete()
    messages.success(request, ' ایمیل حذف شد ')
    return redirect('cms:khabarname_list')

# END ---------KhabarName-----------------------------------

# START-----------------USER--------------------

def UserView(request):
    UserList = MyUser.objects.all()
    context = {
        'users': UserList,
    }
    return render(request, 'cms/user/UserList.html', context)

def detail_user(request, id):
    x = get_object_or_404(MyUser, id=id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=x)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
            return redirect('cms:UserView')
        else:
            print(form.errors)
    else:
        form = UserForm(instance=x)
    context = {
        'form': form,
        'x': x,
        'now': datetime.datetime.now().strftime("%Y-%m-%d"+"T"+"%H:%M"),
    }
    return render(request, 'cms/user/detailuser.html', context)

def CreateUser(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password = make_password(password)
            try:
                MyUser.objects.create(
                    username=username, password=password
                )
            except Exception as e:
                if 'UNIQUE constraint failed: account_myuser.username' in str(e):
                    messages.error(request, 'این نام کاربری قبلا ثبت شده است')
                    return redirect('cms:UserView')
                else:
                    messages.error(
                        request, 'مشکلی پیش امده است لطفا بعدا دوباره تلاش کنید.')
                    return redirect('cms:UserView')

            messages.success(request, 'User جدید با موفقیت اضافه شد')
            return redirect('cms:UserView')
        else:
            print(form.errors)
    else:
        form = UserCreateForm()
    context = {
        'form': form,
        'now': datetime.datetime.now().strftime("%Y-%m-%d"+"T"+"%H:%M"),
    }
    return render(request, 'cms/user/add_user.html', context)

def DeleteUser(request, id):
    x = get_object_or_404(MyUser, id=id)
    x.delete()
    messages.success(request, 'User شما با موفقیت حذف شد')
    return redirect('cms:UserView')

# END-----------------USER--------------------

# START ---------FOOTER ASLI-----------------------------------

def footer_asli_view(request):
    if request.method == 'POST':
        form = FooterAsliForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            footer = FooterAsli.objects.create(name=name)
            messages.success(request, ' فوتر اصلی ' +
                             footer.name + ' اضافه شد ')
            return redirect('cms:footer_list')
        else:
            pass
    else:
        pass
    return render(request, 'cms/footer/footer_asli.html', {})

def list_footer(request):
    footers = FooterAsli.objects.all()
    footer_zir = FooterZir.objects.all()
    context = {
        'footers': footers,
        'footer_zir': footer_zir
    }
    return render(request, 'cms/footer/footer_list.html', context)

def detail_footer_asli(request, id):
    footerasil = get_object_or_404(FooterAsli, id=id)
    if request.method == 'POST':
        form = FooterAsliForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            footer_asli = FooterAsli.objects.filter(
                id=id).update(name=new_name)
            messages.success(request, ' فوتر اصلی به ' +
                             new_name + ' تغییر پیدا کرد ')
            return redirect('cms:footer_list')
        else:
            pass
    context = {
        'footerasil': footerasil
    }
    return render(request, 'cms/footer/footer_asli_detail.html', context)

def delete_footer_asli(request, id):
    footer_asli = get_object_or_404(FooterAsli, id=id)
    try:
        footer_asli.delete()
        messages.success(request, ' فوتر اصلی حذف شد ')
    except Exception as e:
        if "Cannot delete some instances of model 'FooterAsli'" in str(e):
            messages.warning(
                request, 'لطفا قبل از حذف فوتر اصلی , فوتر های فرعی مربوط به ان را حذف کنید')
        else:
            messages.warning(
                request, 'متاسفانه مشکلی در سیستم رخ داده است و لطفا دوباره تلاش کنید')
    return redirect('cms:footer_list')

# END ---------FOOTER ASLI-----------------------------------

# START ---------FOOTER ZIR-----------------------------------

def footer_zir_view(request):
    if request.method == "POST":
        form = FooterZirForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            link = form.cleaned_data['link']
            footer = form.cleaned_data['footer']
            FooterZir.objects.create(name=name, link=link, footer=footer)
            messages.success(request, ' فوتر فرعی ' + name + ' اضافه شد ')
            return redirect('cms:footer_list')
        else:
            print('not yet')
    return render(request, 'cms/footer/footer_zir.html', {'form': FooterZirForm()})

def detail_footer_zir(request, id):
    footer_zir = get_object_or_404(FooterZir, id=id)

    if request.method == 'POST':
        form = FooterZirUpdateForm(request.POST, instance=footer_zir)

        print(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            messages.success(request, ' فوتر فرعی ' + name + ' تغییر کرد ')
            return redirect('cms:footer_list')
        else:
            pass
    else:
        form = FooterZirUpdateForm(instance=footer_zir)
    context = {
        'footer_zir': footer_zir,
        'form': form
    }
    return render(request, 'cms/footer/footer_zir_detail.html', context)

def delete_footer_zir(request, id):
    footer_zir = get_object_or_404(FooterZir, id=id)
    messages.success(request, ' فوتر فرعی ' + footer_zir.name + ' حذف شد ')
    footer_zir.delete()
    return redirect('cms:footer_list')

# END ---------FOOTER ZIR---------------------------------

# START ---------NAVBAR-----------------------------------

def list_nav(request):
    context = {
        'navsone': NavOne.objects.all(),
        'navstwo': NavTwo.objects.all(),
        'navsthree': NavThree.objects.all(),
    }
    return render(request, 'cms/nav/nav_list.html', context)

def nav_one_view(request):
    if request.method == 'POST':
        form = NavOneForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            messages.success(request, ' نوبار سطح یک  ' + name + ' ساخته شد ')
            return redirect('cms:nav_list')
        else:
            pass
    context = {

    }
    return render(request, 'cms/nav/nav_one.html', context)

def detail_nav_one(request, id):
    navone = get_object_or_404(NavOne, id=id)
    if request.method == 'POST':
        form = NavOneForm(request.POST, instance=navone)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            messages.success(request, ' نوبار سطح یک  ' + name + ' تغییر کرد ')
            return redirect('cms:nav_list')
        else:
            print("what?")
    form = NavOneForm(instance=navone)
    context = {
        'form': form,
        'navone': navone,
    }
    return render(request, 'cms/nav/nav_one_detail.html', context)

def delete_nav_one(request, id):
    navone = get_object_or_404(NavOne, id=id)
    try:
        navone.delete()
        messages.success(request, ' نوبار سطح یک  حذف شد ')
    except Exception as e:
        if "Cannot delete some instances of model 'NavOne'" in str(e):
            messages.warning(
                request, 'لطفا قبل از حذف نوبار سطح یک , نوبار های سطح دو مربوط به ان را حذف کنید')
        else:
            messages.warning(
                request, 'متاسفانه مشکلی در سیستم رخ داده است و لطفا دوباره تلاش کنید')
    return redirect('cms:nav_list')

def nav_two_view(request):
    if request.method == 'POST':
        form = NavTwoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            messages.success(request, ' نوبار سطح دو ' + name + ' ساخته شد ')
            return redirect('cms:nav_list')
        else:
            pass
    context = {
        'form': NavTwoForm()
    }
    return render(request, 'cms/nav/nav_two.html', context)

def detail_nav_two(request, id):
    navtwo = get_object_or_404(NavTwo, id=id)
    if request.method == 'POST':
        form = NavTwoForm(request.POST, instance=navtwo)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            messages.success(request, ' نوبار سطح دو  ' + name + ' تغییر کرد ')
            return redirect('cms:nav_list')
        else:
            print("what?")
    form = NavTwoForm(instance=navtwo)
    context = {
        'form': form,
        'navtwo': navtwo,
    }
    return render(request, 'cms/nav/nav_two_detail.html', context)

def delete_nav_two(request, id):
    navtwo = get_object_or_404(NavTwo, id=id)
    # try:
    navtwo.delete()
    messages.success(request, ' نوبار سطح دو  حذف شد ')
    # except Exception as e :
    #     if "Cannot delete some instances of model 'NavTwo'" in str(e):
    #         messages.warning(request, 'لطفا قبل از حذف نوبار سطح یک , نوبار های سطح دو مربوط به ان را حذف کنید')
    #     else :
    #         messages.warning(request, 'متاسفانه مشکلی در سیستم رخ داده است و لطفا دوباره تلاش کنید')
    return redirect('cms:nav_list')

def nav_three_view(request):
    if request.method == 'POST':
        form = NavThreeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            messages.success(request, ' نوبار سطح سه ' + name + ' ساخته شد ')
            return redirect('cms:nav_list')
        else:
            pass
    context = {
        'form': NavThreeForm()
    }
    return render(request, 'cms/nav/nav_two.html', context)

def detail_nav_three(request, id):
    navthree = get_object_or_404(NavThree, id=id)
    if request.method == 'POST':
        form = NavThreeForm(request.POST, instance=navthree)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            messages.success(request, ' نوبار سطح سه  ' + name + ' تغییر کرد ')
            return redirect('cms:nav_list')
        else:
            print("what?")
    form = NavThreeForm(instance=navthree)
    context = {
        'form': form,
        'navthree': navthree,
    }
    return render(request, 'cms/nav/nav_three_datail.html', context)

def delete_nav_three(request, id):
    navthree = get_object_or_404(NavThree, id=id)
    # try:
    navthree.delete()
    messages.success(request, ' نوبار سطح سه حذف شد ')
    # except Exception as e :
    #     if "Cannot delete some instances of model 'NavTwo'" in str(e):
    #         messages.warning(request, 'لطفا قبل از حذف نوبار سطح یک , نوبار های سطح دو مربوط به ان را حذف کنید')
    #     else :
    #         messages.warning(request, 'متاسفانه مشکلی در سیستم رخ داده است و لطفا دوباره تلاش کنید')
    return redirect('cms:nav_list')

# END ---------NAVBAR-----------------------------------

# START------------------SITESETTING------------------

def detail_site_setting(request):
    x = SiteSetting.objects.first()
    if request.method == "POST":
        form = SiteSettingForm(request.POST, request.FILES, instance=x)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
        else:
            pass
    else:
        form = SiteSettingForm(instance=x)
    context = {
        'form': form, 'x': x
    }
    return render(request, 'cms/site_setting_edit.html', context)

# END------------------SITESETTING------------------

# START-----------------SLIDERS----------

def slider_listview(request):
    slider_list = Slider.objects.all()
    context = {
        'slider_list': slider_list,
    }
    return render(request, 'cms/slider/slider_list.html', context)

def slider_add_view(request):
    if request.method == "POST":
        form = SliderForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'اسلایدر جدید با موفقیت اضافه شد')
            return redirect('cms:slider_listview')
        else:
            pass
    else:
        form = SliderForm()
    context = {
        'form': form
    }
    return render(request, 'cms/slider/add_slider.html', context)

def detail_Slider(request, id):
    x = get_object_or_404(Slider, id=id)
    if request.method == "POST":
        form = SliderForm(request.POST, instance=x)
        if form.is_valid():
            messages.success(request, 'اسلایدر  با موفقیت ویرایش شد')
            form.save()
            return redirect('cms:slider_listview')
        else:
            pass
    else:
        form = SliderForm(instance=x)
    context = {
        'form': form,
        'x': x,
    }
    return render(request, 'cms/slider/slider_detail.html', context)

def Delete_Slider(request, id):
    x = get_object_or_404(Slider, id=id)
    x.delete()
    messages.success(request, 'اسلایدر شما با موفقیت حذف شد')
    return redirect('cms:slider_listview')

# END----------------------Slider---------------------

# START ---------TABILGH-----------------------------------

def Tabligh_listview(request):
    Tabligh_list = Tabligh.objects.all()
    context = {
        'tabligh_lists': Tabligh_list,
    }
    return render(request, 'cms/tabligh/tabligh_list.html', context)

def tabligh_view(request):
    if request.method == "POST":
        form = TablighForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'تبلیغ جدید با موفقیت اضافه شد')
            return redirect('cms:tabligh_list')
        else:
            print(form.errors)
    else:
        form = TablighForm()
    context = {
        'form': form
    }
    return render(request, 'cms/tabligh/add_tabligh.html', context)

def detail_Tabligh(request, id):
    x = get_object_or_404(Tabligh, id=id)
    if request.method == "POST":
        form = TablighForm(request.POST, request.FILES, instance=x)
        if form.is_valid():
            form.save()
            messages.success(request, 'تبلیغ با موفقیت ویرایش شد')
            return redirect('cms:tabligh_list')
        else:
            pass
    else:
        form = TablighForm(instance=x)
    context = {
        'form': form, 'x': x
    }
    return render(request, 'cms/tabligh/tabligh_detail.html', context)

def Delete_tabligh(request, id):
    x = get_object_or_404(Tabligh, id=id)
    x.delete()
    messages.success(request, 'تبلیغ با موفقیت حذف شد')
    return redirect('cms:tabligh_list')

# END ---------TABILGH-----------------------------------

# START------------------TAGNEWPAGES------------------

def TagNewPages_listview(request):
    TagNewPage_list = TagNewPage.objects.all()
    context = {
        'tagpages': TagNewPage_list,
    }
    return render(request, 'cms/tagnewpage/tag_new_page_list.html', context)

def New_Tag_Page_Add(request):
    if request.method == "POST":
        form = TagNewPageForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'تگ جدید با موفقیت اضافه شد')
            return redirect('cms:TagNewPages_listview')
        else:
            pass
    else:
        form = TagNewPageForm()
    context = {
        'form': form
    }
    return render(request, 'cms/tagnewpage/add_new_page_tag.html', context)

def detail_tagnewpages(request, id):
    x = get_object_or_404(TagNewPage, id=id)
    if request.method == "POST":
        form = TagNewPageForm(request.POST, instance=x)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
            return redirect('cms:TagNewPages_listview')
        else:
            pass
    else:
        form = TagNewPageForm(instance=x)
    context = {
        'form': form, 'x': x
    }
    return render(request, 'cms/tagnewpage/tag_new_page_detail.html', context)

def Delete_NewTagPage(request, id):
    x = get_object_or_404(TagNewPage, id=id)
    x.delete()
    messages.success(request, 'تگ شما با موفقیت حذف شد')
    return redirect('cms:TagNewPages_listview')

# END------------------NEWTAGPAGES------------------

# START-----------------TAGFOOTER------------------

def TagFooter_listview(request):
    tag_footer = TagFooter.objects.all()
    context = {
        'tag_footer': tag_footer,
    }
    return render(request, 'cms/tagfooter/tag_footer_list.html', context)

def tag_footer_add(request):
    if request.method == "POST":
        form = tag_footer_forms(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'تگ جدید با موفقیت اضافه شد')
            return redirect('cms:TagFooter_listview')
        else:
            pass
    else:
        form = tag_footer_forms()
    context = {
        'form': form
    }
    return render(request, 'cms/tagfooter/tag_footer_add.html', context)

def detail_tag_footer(request, id):
    x = get_object_or_404(TagFooter, id=id)
    if request.method == "POST":
        form = tag_footer_forms(request.POST, instance=x)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
            return redirect('cms:TagFooter_listview')
        else:
            pass
    else:
        form = tag_footer_forms(instance=x)
    context = {
        'form': form, 'x': x
    }
    return render(request, 'cms/tagfooter/tag_footer_detail.html', context)

def delete_tag_footer(request, id):
    x = get_object_or_404(TagFooter, id=id)
    x.delete()
    messages.success(request, 'تگ شما با موفقیت حذف شد')
    return redirect('cms:TagFooter_listview')

# END-------------------TAGFOOTER--------------

# START ---------TAG NAVBAR-----------------------------------

def Tag_navbar_view(request):
    if request.method == "POST":
        form = Tag_navbr_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تگ جدید با موفقیت اضافه شد')
            return redirect('cms:listview_navbar')
        else:
            pass
    else:
        form = Tag_navbr_form()
    context = {
        'form': Tag_navbr_form
    }
    return render(request, 'cms/tag/tag_nav.html', context)

def Tag_navbar_listview(request):
    Tag_list = TagNav.objects.all()
    context = {
        'tag_lists': Tag_list
    }
    return render(request, 'cms/tag/tag_list.html', context)

def detail_tag_navbar(request, id):
    x = get_object_or_404(TagNav, id=id)
    if request.method == "POST":
        form = Tag_navbr_form(request.POST, instance=x)
        if form.is_valid():
            form.save()
            messages.success(request, 'تگ با موفقیت ویرایش شد')
            return redirect('cms:listview_navbar')
        else:
            pass
    else:
        form = Tag_navbr_form(instance=x)
    context = {
        'form': form, 'x': x
    }
    return render(request, 'cms/tag/tag_detail.html', context)

def Delete(request, id):
    x = get_object_or_404(TagNav, id=id)
    x.delete()
    messages.success(request, 'تگ با موفقیت حذف شد')
    return redirect('cms:listview_navbar')

# END ---------TAG NAVBAR-----------------------------------

# START------------------ZirSlider------------------

def zirslider_edit(request):
    x = ZirSlider.objects.first()
    if request.method == "POST":
        form = ZirSliderForm(request.POST, request.FILES, instance=x)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
        else:
            print(form.errors)
    else:
        form = ZirSliderForm(instance=x)
    context = {
        'form': form, 'x': x
    }
    return render(request, 'cms/zirslider_edit.html', context)

# END------------------ZirSlider------------------

# START ---------Category -----------------------------------

def category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'یک دسته بندی اضافه شد ')
            return redirect('cms:category_list')
        else:
            print(form.errors)
            messages.error(
                request, 'مشکلی پیش امده است لطفا دوباره تلاش کنید.')
            return redirect('cms:category_list')
    else:
        form = CategoryForm()
    context = {
        'form': form
    }
    return render(request, 'cms/category/category_view.html', context)

def list_category(request):
    categorys = Category.objects.all()
    context = {
        'categorys': categorys,
    }
    return render(request, 'cms/category/category_list.html', context)

def detail_category_asli(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'مشخصات دسته بندی تغییر پیدا کرد ')
            return redirect('cms:category_list')
        else:
            messages.error(
                request, 'مشکلی پیش امده است لطفا دوباره تلاش کنید.')
            return redirect('cms:category_list')
    else:
        form = CategoryForm(instance=category)
    context = {
        'category': category,
        'form': form
    }
    return render(request, 'cms/category/category_detail.html', context)

def category_asli(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    messages.success(request, ' دسته بندی حذف شد ')
    return redirect('cms:category_list')

# END ---------Category -----------------------------------

# START ---------zircategory-----------------------------------

def zircategory_view(request):
    if request.method == "POST":
        form = ZirCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' زیر دسته بندی اضافه شد ')
            return redirect('cms:zircategory_list')
        else:
            print('not yet')
    else :
        form = ZirCategoryForm()
    context = {
        'form': form
    }
    return render(request, 'cms/zircategory/zircategory_view.html', context)

def list_zircategory(request):
    zircategorys = ZirCategory.objects.all()
    context = {
        'zircategorys': zircategorys,
    }
    return render(request, 'cms/zircategory/zircategory_list.html', context)

def detail_zircategory(request, id):
    zircategory = get_object_or_404(ZirCategory, id=id)
    if request.method == 'POST':
        form = ZirCategoryForm(request.POST, instance=zircategory)
        if form.is_valid():
            form.save()
            messages.success(request, ' زیردسته تغییر کرد ')
            return redirect('cms:zircategory_list')
        else:
            pass
    else:
        form = ZirCategoryForm(instance=zircategory)
    context = {
        'zircategory': zircategory,
        'form': form
    }
    return render(request, 'cms/zircategory/zircategory_detail.html', context)

def delete_zircategory(request, id):
    zircategory = get_object_or_404(ZirCategory, id=id)
    messages.success(request, ' زیر دسته ' + zircategory.name + ' حذف شد ')
    zircategory.delete()
    return redirect('cms:zircategory_list')

# END ---------zircategory---------------------------------

# START-----------------TAGPRODUCT------------------

def tags_listview(request):
    tags = Tags.objects.all()
    context = {
        'tags': tags,
    }
    return render(request, 'cms/tags/tags_list.html', context)

def tags_add(request):
    if request.method == "POST":
        form = TagsForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'تگ جدید با موفقیت اضافه شد')
            return redirect('cms:tags_listview')
        else:
            pass
    else:
        form = TagsForm()
    context = {
        'form': form
    }
    return render(request, 'cms/tags/tags_add.html', context)

def detail_tags(request, id):
    x = get_object_or_404(Tags, id=id)
    if request.method == "POST":
        form = TagsForm(request.POST, instance=x)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
            return redirect('cms:tags_listview')
        else:
            pass
    else:
        form = TagsForm(instance=x)
    context = {
        'form': form, 'x': x
    }
    return render(request, 'cms/tags/tags_detail.html', context)

def delete_tags(request, id):
    x = get_object_or_404(Tags, id=id)
    x.delete()
    messages.success(request, 'تگ شما با موفقیت حذف شد')
    return redirect('cms:tags_listview')

# END-------------------TAGPRODUCT--------------

# START----------------PRODUCT------------------

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'cms/product/product_list.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
            return redirect('cms:product_detail',id=id)
        else:
            print(form.errors)
            if 'Ensure this value is less than or equal to 100' in str(form.errors):
                messages.error(request, 'تخفیف باید بین 0 تا 100 باشد' )
            else :
                messages.error(request, 'مشکلی پیش امده است لطفا دوباره امتحان کنید.' ) 
    else:
        form = ProductForm(instance=product)
        size_form = SizeForm()
        color_form = ColorForm()
        image_form = GalleryImageForm()
    context = {
        'product': product,
        'form': form, 
        'size_form':size_form,
        'color_form':color_form,
        'image_form':image_form,
    }
    return render(request, 'cms/product/product_detail.html', context)

def product_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'محصول جدید با موفقیت اضافه شد')
            return redirect('cms:product_list')
        else:
            print(form.errors)
            if 'Ensure this value is less than or equal to 100' in str(form.errors):
                messages.error(request, 'تخفیف باید بین 0 تا 100 باشد' )
            else :
                messages.error(request, 'مشکلی پیش امده است لطفا دوباره امتحان کنید.' ) 
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'cms/product/product_view.html', context)

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    try:
        product.delete()
        messages.success(request, 'محصول شما با موفقیت حذف شد')
    except ProtectedError:
        messages.error(request, 'لطفا قبل از حذف محصول عکس ها , رنگ ها و سایز های اضافی ان را حذف کنید' ) 
        return redirect('cms:product_detail',id=id)
    except Exception as e:
        print(e,e.__class__.__name__,'test')
        messages.error(request, 'مشکلی پیش امده است لطفا دوباره امتحان کنید.' )     
    return redirect('cms:product_list')

def product_zircat_ajax(request):
    try:
        cat_id = request.GET.get('cat_id')
        zircats_id = ZirCategory.objects.filter(Category_asli__id=cat_id).values_list('id',flat=True)
        zircats_name = ZirCategory.objects.filter(Category_asli__id=cat_id).values_list('name',flat=True)
        zircats = zip(zircats_id,zircats_name)
    except ValueError:
        zircats = ''
    return JsonResponse({'zircats':dict(zircats)})

def product_add_size(request):
    if request.method == 'POST':
        
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        product.size_set.all().delete()
        
        size_deleted_list = request.POST.getlist('is_delete')
        size_name_list = request.POST.getlist('size')
        size_ekhtelaf_list = request.POST.getlist('Ekhtelaf')
        size_list = dict(zip(size_name_list,size_ekhtelaf_list))
        
        Size.objects.bulk_create([
            Size(product=product,size=size,Ekhtelaf=size_list[size])\
            for size in size_list\
            if size not in size_deleted_list 
            ])
        # for size in size_list:
        #     if size not in size_deleted_list:
        #         Size.objects.create(product=product,size=size,Ekhtelaf=size_list[size])
        
        messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
        return redirect('cms:product_detail',id=product_id)
    else:
        messages.error(request, 'مشکلی پیش امده است لطفا دوباره امتحان کنید.' )
        return redirect('cms:product_list') 

def product_add_color(request):
    if request.method == 'POST':
        
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        product.color_set.all().delete()
        
        color_deleted_list = request.POST.getlist('is_delete')
        color_name_list = request.POST.getlist('color')
        color_ekhtelaf_list = request.POST.getlist('Ekhtelaf')
        color_list = dict(zip(color_name_list,color_ekhtelaf_list))
        
        Color.objects.bulk_create([
            Color(product=product,color=color,Ekhtelaf=color_list[color])\
            for color in color_list\
            if color not in color_deleted_list 
            ])
        # for color in color_list:
        #     if color not in color_deleted_list:
        #         Color.objects.create(product=product,color=color,Ekhtelaf=color_list[color])
        
        messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
        return redirect('cms:product_detail',id=product_id)
    else:
        messages.error(request, 'مشکلی پیش امده است لطفا دوباره امتحان کنید.' )
        return redirect('cms:product_list') 

def product_add_image(request):
    if request.method == 'POST':
        
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        
        image_deleted_list = request.POST.getlist('is_delete')
        image_name_list = request.FILES.getlist('image')
        image_alt_list = request.POST.getlist('alt')
        image_list = dict(zip(image_name_list,image_alt_list))
        
        # delete checkmarked images
        for image in image_deleted_list:
            GalleryImage.objects.filter(image=image).delete()  
        
        #create new image
        for image in image_list : 
            x = GalleryImage.objects.bulk_create([
                GalleryImage(product=product,image=image,alt=image_list[image]) 
                ])
            # save thumnail for new images
            x[0].save()

           
        messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
        return redirect('cms:product_detail',id=product_id)
    else:
        messages.error(request, 'مشکلی پیش امده است لطفا دوباره امتحان کنید.' )
        return redirect('cms:product_list')

def product_changealt_ajax(request):
    print(request.GET)
    img = request.GET.get('img')
    alt = request.GET.get('val')
    id = request.GET.get('id')
    product = Product.objects.get(id = id)
    product.galleryimage_set.filter(image=img).update(alt=alt)
    messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
    return JsonResponse({})

def search_name(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        products = Product.objects.filter(name__icontains=name)
    context = {
        'products': products,
    }
    return render(request, 'cms/product/product_list.html', context) 
# END----------------PRODUCT------------------

# START-----------------COMMENT------------------

def comment_listview(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments,
    }
    return render(request, 'cms/comment/comment_list.html', context)

def detail_comment(request, id):
    x = get_object_or_404(Comment, id=id)
    if request.method == "POST":
        form = CommentFormCMS(request.POST, instance=x)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
            return redirect('cms:comment_listview')
        else:
            pass
    else:
        form = CommentFormCMS(instance=x)
    context = {
        'form': form, 'x': x
    }
    return render(request, 'cms/comment/comment_detail.html', context)

def delete_comment(request, id):
    x = get_object_or_404(Comment, id=id)
    x.delete()
    messages.success(request, 'تگ شما با موفقیت حذف شد')
    return redirect('cms:comment_listview')

# END-------------------COMMENT--------------
