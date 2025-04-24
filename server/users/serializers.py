from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)

    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True, max_length=150, blank=True)
    last_name = serializers.CharField(required=True, max_length=150, blank=True)
    email = serializers.CharField(required=True, max_length=150, blank=True)
    is_staff = serializers.BooleanField(
        default=False,
        required=False,
    )
    is_active = serializers.BooleanField(
        default=True,
        required=False,
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active')

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()
        return instance