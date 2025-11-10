from django.shortcuts import render
from .models import Category, Product
from django.http import JsonResponse,Http404


# Create your views here.

def index(request, category_id = None):
    categories = Category.objects.all()
    
    if category_id is None:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category_id=category_id)
        
        
    
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'app/home.html', context)

def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    if not product:
        return JsonResponse({'error': 'Product not found'}, status=404)
    
    context = {
        'product': product
    }
    
    return  render(request, 'app/detail.html', context)


@property
def get_img_url(self):
    if not self.image:
        return
    
    return self.image.url


def __str__(self):
    return self.name