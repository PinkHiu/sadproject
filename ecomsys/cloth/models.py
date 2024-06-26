from django.db import models

from product.models import Product


class Cloth(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    brand = models.CharField(max_length=255)
    size = models.CharField(max_length=10)
    image = models.ImageField(upload_to="cloth_images/")

    class Meta:
        verbose_name_plural = "Clothes"
