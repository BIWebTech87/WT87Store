from django.urls import path, include
from .views import ProductsViewSet

app_name = 'products'

urlpatterns = [
    path('', ProductsViewSet.as_view({
        'get': 'list',
    }) , name="products"),
]