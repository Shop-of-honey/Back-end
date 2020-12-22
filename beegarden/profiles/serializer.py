from rest_framework import serializers

from profiles.models import Product, User
from django_restql.mixins import DynamicFieldsMixin


class UserAunSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', "email", "phone")


class ProductSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    creator = UserSerializer(read_only=True, fields=["email", "phone", "first_name", "last_name"])

    class Meta:
        model = Product
        fields = ("id", "name", "description", "creator", "price", "location")


class UserDetailsSerializer:
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'description')
        read_only_fields = ('email',)
