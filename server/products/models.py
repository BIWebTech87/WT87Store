from django.db import models
from django.utils.translation import gettext_lazy as _

class Size(models.TextChoices):
    select = 'select', _('Select')
    XS = 'XS', _('Extra Small')
    S = 'S', _('Small')
    M = 'M', _('Medium')
    L = 'L', _('Large')
    XL = 'XL', _('Extra Large')
    XXL = 'XXL', _('Extra Extra Large')

class Color(models.TextChoices):
    select = 'select', _('Select')
    black = 'black', _('Black')
    white = 'white', _('White')

class Category(models.TextChoices):
    select = 'select', _('Select')
    cloth = 'cloth', _('Cloth')
    accessories = 'accessories', _('Accessories')

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    color = models.CharField(max_length=255, choices=Color.choices, default=Color.select)
    size = models.CharField(max_length=255, choices=Size.choices, default=Size.select)
    stock = models.IntegerField()
    category = models.CharField(max_length=255, choices=Category.choices, default=Category.select)
    image = models.ImageField(upload_to='products/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
