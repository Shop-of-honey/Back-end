from rest_framework import serializers

from profiles.models import Product, User
from django_restql.mixins import DynamicFieldsMixin


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', "email", "phone")


class ProductSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        creator = UserSerializer(read_only=True, fields=["email"])

        model = Product
        fields = ("id", "name", "description", "creator", "price", "location")


class UserDetailsSerializer:

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'email', 'phone')
