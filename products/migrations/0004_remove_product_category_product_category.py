# Generated by Django 4.2.1 on 2023-05-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(default='Non Categorized', to='products.category'),
        ),
    ]
