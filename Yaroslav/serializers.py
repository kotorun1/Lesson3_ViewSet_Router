from rest_framework import serializers
from .models import Pet, Order, Category, StatusPet, Type, StatusOrder

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'category', 'name', 'photo', 'status', 'type')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'pet', 'quantity', 'ship_date', 'status', 'complete')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class StatusPetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusPet
        fields = ('id', 'name')

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')

class StatusOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusOrder
        fields = ('id', 'name')

