# Generated by Django 4.0.4 on 2022-07-19 23:02

from django.db import migrations, models
import store.enums


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[(store.enums.CategoryTypes['SPORTS'], 'Sports'), (store.enums.CategoryTypes['ELECTRONICS'], 'Electronics'), (store.enums.CategoryTypes['BOOK'], 'Book')], max_length=100),
        ),
    ]
