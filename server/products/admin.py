from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Product


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    list_display = [
        "name",
        "price",
        "description",
        "color",
        "size",
        "stock",
        "category",
        "image",
        "created_at",
        "updated_at",
    ]


admin.site.register(Product, ProductAdmin)
