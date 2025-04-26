from django.contrib.auth.password_validation import get_password_validators
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True, max_length=150)
    last_name = serializers.CharField(required=True, max_length=150)
    email = serializers.CharField(required=True, max_length=150)
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
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'password')

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": f"User with username '{username}' already exists."}
            )

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {"email": f"User with email '{email}' already exists."}
            )

        try:
            password = validated_data.pop('password')
            new_user = User.objects.create(**validated_data)
            new_user.set_password(password)
            new_user.save()
            return new_user
        except Exception as e:
            raise serializers.ValidationError({"error": str(e)})

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance
