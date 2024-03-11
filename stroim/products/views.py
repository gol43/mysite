from django.shortcuts import render
from .models import Product
from .utils import paginate

PAGE_FOR_LIST = 8

def index(request):
    template = 'products/index.html'
    return render(request, template) 

def products_list(request):
    products = Product.objects.all()
    page_obj = paginate(request, products, PAGE_FOR_LIST)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'products/products_list.html', context)