from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages  # Импортируем messages для вывода сообщений об ошибках
from .models import Product, Category
from .utils import paginate
from .forms import CommentForm

PAGE_FOR_LIST = 8

def index(request):
    template = 'products/index.html'
    return render(request, template) 

def products_list(request):
    product = Product.objects.all()
    page_obj = paginate(request, product, PAGE_FOR_LIST)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'products/products_list.html', context)


def products_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    title = 'Пост'
    context = {
        'product': product,
        'title': title,
    }
    return render(request, 'products/products_detail.html', context)

def add_comment(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.product = product
            comment.save()
            return redirect('products:products_detail', product_id=product_id)
        else:
            messages.error(request, 'Пожалуйста, напишите комментарий')  
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'products/comment_form.html', context)


def comment_form(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = CommentForm()
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'products/comment_form.html', context)


def category_list(request, category_id):
    category_name = Category.objects.get(id=category_id)
    product = Product.objects.filter(category=category_name)
    page_obj = paginate(request, product, PAGE_FOR_LIST)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'products/category_list.html', context)

