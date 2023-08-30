from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect

from Product.models import Product, Category
from Product.forms import ReviewForm, ProductCreateForm, CategoryCreateForm

# Основной вид
def main_view(request):
    return render(request, 'layouts/index.html')


# Вид продукта
def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context_data = {
            "products": products
        }
        return render(request, 'products/products.html', context=context_data)


# Вид категории
def category(request):
    categories = Category.objects.all()
    context_data = {
        "categories": categories
    }
    return render(request, 'categories/categories.html', context=context_data)


# Подробное представление продукта
def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return HttpResponseRedirect(f'/product/{id}/')
    else:
        form = ReviewForm()
    context_data = {
        "product": product,
        "form": form
    }
    return render(request, 'products/detail.html', context=context_data)


# БЛОК ПОЛЬЗОВАТЕЛЬСКИХ СТРАНИЦ #

# Создание продукта пользователем
def create_product(request):
    if request.method == 'POST':
        product_form = ProductCreateForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('product_detail_view', id=product_form.instance.id)
    else:
        product_form = ProductCreateForm()
    return render(request, 'products/create_product.html', {'product_form': product_form})


# Создание категории пользователем
def create_category(request):
    if request.method == 'POST':
        category_form = CategoryCreateForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return redirect('category')
    else:
        category_form = CategoryCreateForm()
    return render(request, 'categories/create_categories.html', {'category_form': category_form})

# БЛОК ПОЛЬЗОВАТЕЛЬСКИХ СТРАНИЦ #