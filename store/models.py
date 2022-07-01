from django.db import models
from polymorphic.models import PolymorphicModel


class Category(PolymorphicModel):
    pass


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        to=Category, related_name="products", on_delete=models.CASCADE
    )
