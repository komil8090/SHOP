

from django.shortcuts import render ,redirect,get_object_or_404
from .models import Category , Product , Comment
from django.http import JsonResponse
from app.forms import ProductModelForm, ProductForm,OrderModelForm,CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q
from app.utils import filter_by_price


# Create your views here.


def index(request,category_id = None):
    
    categories = Category.objects.all()
    
    if category_id:
        products = Product.objects.filter(category = category_id)
    else:
        products = Product.objects.all()
    
    
    context = {
        'categories':categories,
        'products':products
    }
    return render(request,'app/home.html',context)



def detail(request,pk):
    product = Product.objects.get(id = pk)
    if not product:
        return JsonResponse(data={'message':'Oops. Page Not Found','status_code':404})
    
    context = {
        'product' : product
    }
    return render(request,'app/detail.html',context)



# name = request.POST.get('name')



@login_required(login_url='/admin/')
def create_product(request):
    if request.method == 'POST':
        form = ProductModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Product successfully created ✅"
            )
            # add messages
            
            return redirect('app:create')
    else:
        form = ProductModelForm()
        
                
    context = {
        'form':form
    }
    return render(request,'app/create.html',context)


def delete_product(request,pk):
    product = Product.objects.get(id = pk)
    if product:
        product.delete()
        return redirect('app:index')    
    
    return render(request,'app/detail.html')



def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("app:detail", product_id=product.id)
    else:
        form = ProductForm(instance=product)

    return render(request, "app/edit_product.html", {"form": form, "product": product})


def create_order(request,pk):
    product = get_object_or_404(Product,pk=pk)

    if request.method == 'POST':
        print('Order Post sending ....')
        form = OrderModelForm(request.POST)
        if form.is_valid():
            print('form valid')
            order = form.save(commit=False)
            order.product = product
            if order.quantity > product.stock:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Dont enough quantity'
                ) 
            else:
                product.stock -= order.quantity 
                print('order valid ')
                product.save()
                order.save()
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Order successfully sent✅'
                ) 
                return redirect('app:detail',product_id=product.id)
    else:
        form = OrderModelForm()

    context = {
        'form':form,
        'product':product
    }

    return render(request,'app/detail.html',context)


def comment_list(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all()

    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")
        Comment.objects.create(product=product, name=name, text=text)
        return redirect('app:detail', pk=pk)

    return render(request, 'app/detail.html', {
        'product': product,
        'comments': comments
    })
