from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.color = validated_data.get('color', instance.color)
        instance.size = validated_data.get('size', instance.size)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.category = validated_data.get('category', instance.category)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance