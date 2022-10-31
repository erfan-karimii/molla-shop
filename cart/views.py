from django.shortcuts import render,get_object_or_404,redirect
from .models import Order,OrderDetail
from product.models import Product
from .forms import NewOrderForm
from django.http import HttpResponse
import json
from django.utils import timezone
# from account.models import Profile
# Create your views here.

def total_priceCA(product_id,color,size):
    price_color = 0
    product = Product.objects.get(id=product_id)
    try:
        x = product.color_set.get(color=color)
        price_color = x.Ekhtelaf
    except:
        pass
    price_size = 0
    try:
        x = product.size_set.get(size=size)
        price_size = x.Ekhtelaf
    except:
        pass
    return price_color + price_size + product.main_discount_cal(inti=True)

def add_user_order(request):
    form = NewOrderForm(request.POST or None)
    if form.is_valid():
        product_id =form.cleaned_data['product_id']    
        color = form.cleaned_data['color']
        size =form.cleaned_data['size']
        count = form.cleaned_data['count']
        
        total_price = total_priceCA(product_id,color,size)
        
        product = Product.objects.get(id=product_id)
        if count < 1 or count > product.tedad_mahsol : 
            return redirect('/')
        
        try:
            x = request.COOKIES['OrderDetail']
            y = request.COOKIES['Order']
            jsonstyle = json.loads(x)
            order = Order.objects.create(id=y)
            orderdetail = OrderDetail.objects.create(order=order,product=product,color=color,count=count,size=size,price=total_price)
            order.delete()

            for x in jsonstyle:
                if jsonstyle[x]['id'] == product_id and jsonstyle[x]['color'] == color and jsonstyle[x]['size'] == size:
                    jsonstyle[x] = {'id':product_id,'color':color,'size':size,'count':count}
                    break
            else:
                jsonstyle[orderdetail.id] = {'id':product_id,'color':color,'size':size,'count':count}

            orderdetail.delete()
            jsonstyle2 = json.dumps(jsonstyle)
            response = redirect('/cart')
            response.delete_cookie('OrderDetail')
            response.set_cookie('OrderDetail',jsonstyle2,172800)
            return response 
        except Exception as e:
            print(e)
            order = Order.objects.create()
            orderdetail = OrderDetail.objects.create(order=order,product=product,color=color,count=count,size=size,price=total_price)
            x = {orderdetail.id:{'id':product_id,'color':color,'size':size,'count':count}}
            orderdetail.delete()
            jsonstyle = json.dumps(x)
            response = redirect('/cart')
            response.set_cookie('OrderDetail',jsonstyle,172800)
            response.set_cookie('Order',order.id,172800)
            order.delete()
            return response 
    else:
        print(form.errors)
        return redirect('/')

def user_open_order(request):
    context = {
    'form': NewOrderForm() ,
    'order':None,
    'details':None,
    'total':0,
    'sum':0,
    }
    total_price = 0
    try:
        detail = request.COOKIES['OrderDetail']
        z = json.loads(detail)
        for det in z:
            id = z[det]['id']
            product = Product.objects.get(id=id)
            if z[det]['count'] > product.tedad_mahsol:
                z[det]['count'] = product.tedad_mahsol

            total_price_single = total_priceCA(z[det]['id'],z[det]['color'],z[det]['size'])
            total_price += total_price_single * z[det]['count']

        context['details'] = z
        context['total'] = total_price
    except:
        print("erer")
    return render(request,'cart.html',context)

def remove_from_cookie(request,id):
    x = request.COOKIES['OrderDetail']
    f = json.loads(x)
    del f[str(id)]
    m = json.dumps(f)
    response = redirect('/cart')
    response.delete_cookie('OrderDetail')
    response.set_cookie('OrderDetail',m,172800)
    return response


def update_In_open_order(request):
    form = NewOrderForm(request.POST or None)
    if form.is_valid():
        product_id =form.cleaned_data['product_id']    
        color = form.cleaned_data['color']
        size =form.cleaned_data['size']
        count = form.cleaned_data['count']
        
        product = Product.objects.get(id=product_id)
        
        if count < 1 or count > product.tedad_mahsol : 
            return redirect('/cart/')
        
        total_price = total_priceCA(product_id,color,size)

        try:
            x = request.COOKIES['OrderDetail']
            jsonstyle = json.loads(x)
            # orderdetail = OrderDetail.objects.create(product=product,color=color,count=count,size=size,price=total_price)
            
            for x in jsonstyle:
                print(color)
                print(size)
                print(product_id)
                if jsonstyle[x]['id'] == product_id and jsonstyle[x]['color'] == color and jsonstyle[x]['size'] == size:
                    jsonstyle[x] = {'id':product_id,'color':color,'size':size,'count':count}
            # orderdetail.delete()
            jsonstyle2 = json.dumps(jsonstyle)
            response = redirect('/cart')
            response.delete_cookie('OrderDetail')
            response.set_cookie('OrderDetail',jsonstyle2,172800)
            return response 
        except:
            order = Order.objects.create()
            orderdetail = OrderDetail.objects.create(product=product,color=color,count=count,size=size,price=total_price)
            x = {orderdetail.id:{'id':product_id,'color':color,'size':size,'count':count}}
            orderdetail.delete()
            jsonstyle = json.dumps(x)
            response = redirect('/cart')
            response.set_cookie('OrderDetail',jsonstyle,172800)
            response.set_cookie('Order',order.id,172800)
            order.delete()
            return response 
    else:
        print('test')
        return redirect('/')
