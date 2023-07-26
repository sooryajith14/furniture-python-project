from django.shortcuts import render, get_object_or_404

from .models import Product
from furn_app .models import Category


# Create your views here.
def store(request,category_slug=None):
    categories=None
    products=None
    if category_slug != None:
        categories=get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=categories,is_available=True)
    else:
        products=Product.objects.all().filter(is_available=True)
    context={
        'products':products,
    }
    return render(request,'store/store.html',context)



def product_details(request,category_slug,product_slug):
        single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
        return render(request,'store/product_details.html',{'single_product':single_product})