from rest_framework import serializers

from .models import Product, Ingredient, Author, Book


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ("name", "ingredients",)


class BookToSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ("id", "title", "description")


class AuthorSerializer(serializers.ModelSerializer):
    books = BookToSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ("id", "name", "biography", "books")
        extra_kwargs = {'books': {'required': False}}


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ("id", "title", "description", "authors")
        extra_kwargs = {'authors': {'required': False}}
