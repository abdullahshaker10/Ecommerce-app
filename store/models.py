from distutils.command.upload import upload
from django.db import models

from store.enums import CategoryTypes
from users.models import CustomUser
from django_extensions.db.models import TimeStampedModel


class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=CategoryTypes.choices())


class Product(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        to=Category, related_name="products", on_delete=models.CASCADE
    )
    price = models.DecimalField(decimal_places=2, max_digits=2, null=True, blank=True)
    vendor = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="products"
    )
    image = models.ImageField(upload_to="images/")
