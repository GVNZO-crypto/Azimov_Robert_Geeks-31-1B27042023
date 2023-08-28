from django import forms
from .models import Category
from .models import Product
from .models import Review


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image','title', 'description', 'category', 'price', 'rate']

        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'rating', 'comment']