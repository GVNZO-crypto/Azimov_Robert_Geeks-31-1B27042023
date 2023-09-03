from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.db.models import Q

from Product.models import Product, Category
from Product.forms import ReviewForm, ProductCreateForm, CategoryCreateForm
from Product.constans import PAGINATION_LIMIT

# Основной вид
def main_view(request):
    # Возвращает главную страницу
    return render(request, 'layouts/index.html')

# Вид продукта
def product_view(request):
    if request.method == 'GET':
        # Получаем параметры поиска и номер страницы
        search = request.GET.get('search')
        page = int(request.GET.get('page',1))
        # Получаем все продукты из базы данных
        products = Product.objects.all()
        # Вычисляем максимальное количество страниц
        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page)< max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)
        # Если задан параметр поиска, фильтруем продукты
        if search:
            products = products.filter(Q(title__icontains=search) | Q(description__icontains=search))
        products = products[PAGINATION_LIMIT* (page-1):PAGINATION_LIMIT* page]
        context_data = {
            "products": products,
            "pages": range(1, max_page+1)
            }
        # Возвращаем страницу с продуктами
        return render(request, 'products/products.html', context=context_data)

# Вид категории
def category(request):
    # Получаем все категории из базы данных
    categories = Category.objects.all()
    context_data = {
        "categories": categories
    }
    # Возвращаем страницу с категориями
    return render(request, 'categories/categories.html', context=context_data)

# Подробное представление продукта
def product_detail_view(request, id):
    # Получаем продукт по его id
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        # Если метод POST, обрабатываем форму отзыва
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return HttpResponseRedirect(f'/product/{id}/')
    else:
        # Если метод GET, отображаем форму отзыва
        form = ReviewForm()
    context_data = {
        "product": product,
        "form": form
    }
    # Возвращаем страницу с подробной информацией о продукте
    return render(request, 'products/detail.html', context=context_data)

# БЛОК ПОЛЬЗОВАТЕЛЬСКИХ СТРАНИЦ #

# Создание продукта пользователем
def create_product(request):
    if request.method == 'POST':
        # Если метод POST, обрабатываем форму создания продукта
        product_form = ProductCreateForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('product_detail_view', id=product_form.instance.id)
    else:
        # Если метод GET, отображаем форму создания продукта
        product_form = ProductCreateForm()
    # Возвращаем страницу создания продукта
    return render(request, 'products/create_product.html', {'product_form': product_form})

# Создание категории пользователем
def create_category(request):
    if request.method == 'POST':
        # Если метод POST, обрабатываем форму создания категории
        category_form = CategoryCreateForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return redirect('category')
    else:
        # Если метод GET, отображаем форму создания категории
        category_form = CategoryCreateForm()
    # Возвращаем страницу создания категории
    return render(request, 'categories/create_categories.html', {'category_form': category_form})

# БЛОК ПОЛЬЗОВАТЕЛЬСКИХ СТРАНИЦ #
