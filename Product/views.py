from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.
from Product.models import Product
from Product.models import Category
from Product.models import Product
from Product.forms import ReviewForm

def main_view(request):
    return render(request, 'layouts/index.html')

def product_view(request):
    if request.method == 'GET':
        product = Product.objects.all
        context_data ={
            "products": product
            }
        return render(request,'products\products.html',context=context_data)

def product_detail_view(request,id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        context_data = {
            "product": product
        }
        return render(request,'products\detail.html',context=context_data)

def category(request):
    categories = Category.objects.all()
    context_data = {
        "categories": categories
    }
    return render(request, 'categories.html', context=context_data)


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