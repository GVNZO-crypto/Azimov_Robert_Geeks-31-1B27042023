from django.shortcuts import HttpResponse, render
# Create your views here.
from Product.models import Product

def main_view(request):
    return render(request, 'layouts/index.html')

def product_view(request):
    if request.method == 'GET':
        product = Product.objects.all
        context_data ={
            "products": product
        }
        return render(request,'products\products.html',context=context_data)