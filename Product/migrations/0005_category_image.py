# Generated by Django 4.2.4 on 2023-08-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_alter_product_image_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images'),
        ),
    ]