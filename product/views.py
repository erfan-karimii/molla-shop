from django.shortcuts import redirect, render,get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Product,Color,Size,Tags,Category,Comment
from .forms import CommentForm
from cart.forms import NewOrderForm
from django.http import JsonResponse

def listView(request):
    contact_list = Product.objects.filter(is_active=True)
    paginator = Paginator(contact_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    sizes = Size.objects.all().distinct()
    context = {
        'products':page_obj,
        'categorys':Category.objects.all(),
        'contact_list':contact_list,
        'paginator':paginator,
        'sizes' : sizes,
    }
    return render(request,'listview.html',context)

def detailview(request,id):
    x = get_object_or_404(Product,id=id)
    form = NewOrderForm(initial={'product_id':x.id})
    context = {
        'x':x,
        'colors': Color.objects.all(),
        'sizes': Size.objects.all(),
        'tags': Tags.objects.all(),
        'form':form,
    }
    return render(request,'product.html',context)
# compare
def compare(request):
    return render(request,'compare.html',{})

def compare_1(request,id):
    product = get_object_or_404(Product,id=id)
    context = {
        'product_1' : product
    }
    return render(request,'compare.html',context)

def compare_listview(request,id,cat):
    contact_list = Product.objects.filter(is_active=True,category__name=cat)
    context = {
        'categorys':Category.objects.all(),
        'contact_list':contact_list,
    }
    return render(request,'compare_listview.html',context)

def compare_2(request,id):
    product_id = request.META.get('HTTP_REFERER').split('/')[-2]
    product_1 = get_object_or_404(Product,id=product_id)
    product_2 = get_object_or_404(Product,id=id)
    context = {
        'product_2' : product_2,
        'product_1' : product_1,
    }
    return render(request,'compare.html',context)
# endcompare
def comment_view(request):
    if request.method == 'POST':
        print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '.نظر شما با موفقیت ثبت شد و بعذ از تایید منتشر میشود')
        else:
            print(form.errors)
    else : 
        print('what?')
    return redirect(request.META.get('HTTP_REFERER'))

def size_name_ajax(request):
    category = request.GET.get('category')
    sizes = Product.objects.filter(category__name=category).distinct().values_list('size_asli')
    sizes = list(sizes)
    json = {'sizes':sizes}
    return JsonResponse(json)
