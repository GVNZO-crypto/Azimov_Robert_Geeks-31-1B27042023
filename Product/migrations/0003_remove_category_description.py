# Generated by Django 4.2.4 on 2023-08-27 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_category_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
