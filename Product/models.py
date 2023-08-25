from django.db import models
# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    rate = models.FloatField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)