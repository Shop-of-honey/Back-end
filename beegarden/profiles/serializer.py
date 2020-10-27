from rest_framework import serializers

from profiles.models import Product, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', "email", "phone")


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        creator = UserSerializer(read_only=True)

        model = Product
        fields = ("id", "name", "description", "creator", "price")


class UserDetailsSerializer:

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'email', 'phone')
