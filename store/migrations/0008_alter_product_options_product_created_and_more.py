# Generated by Django 4.0.4 on 2022-07-19 23:05

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_category_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'get_latest_by': 'modified'},
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=None, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]