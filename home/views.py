from unicodedata import category
from django.shortcuts import render
from django.contrib import messages
from .models import Slider , NavOne, SiteSetting , ZirSlider , Tabligh , FooterAsli
from product.models import Color, Product,ZirCategory
# Create your views here.
def home(request):
	shoese=Product.objects.filter(is_active=True,category__name='کفش')
	context = {
		'sliders' : Slider.objects.all(),
		'zirslider' : ZirSlider.objects.all().last(),
		'tabligh' : Tabligh.objects.all().last(),
		'bags':Product.objects.filter(is_active=True,category__name='کیف'),
		'colorbag':Color.objects.all(),
		'shoese':shoese,
		'shoes_category':ZirCategory.objects.filter(Category_asli__name='کفش'),
		}
	return render(request,'index.html',context)

def header(request):
    context = {
		'navones': NavOne.objects.all(),
		'sitesetting' : SiteSetting.objects.filter(active=True).last(),
	}
    return render(request,'header.html',context)

def footer(request):
    context = {
		'footeraslis': FooterAsli.objects.all(),
		'sitesetting' : SiteSetting.objects.filter(active=True).last(),
	}
    return render(request,'footer.html',context)