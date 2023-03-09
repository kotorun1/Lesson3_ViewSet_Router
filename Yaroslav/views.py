from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Pet, Order, Category, StatusPet, Type, StatusOrder
from .serializers import PetSerializer, OrderSerializer, CategorySerializer, StatusPetSerializer, TypeSerializer, StatusOrderSerializer


class PetList(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetDetail(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class PetCreate(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class OrderList(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderCreate(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreate(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StatusPetList(viewsets.ModelViewSet):
    queryset = StatusPet.objects.all()
    serializer_class = StatusPetSerializer

class StatusPetDetail(viewsets.ModelViewSet):
    queryset = StatusPet.objects.all()
    serializer_class = StatusPetSerializer

class StatusPetCreate(viewsets.ModelViewSet):
    queryset = StatusPet.objects.all()
    serializer_class = StatusPetSerializer

class TypeList(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeDetail(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeCreate(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class StatusOrderList(viewsets.ModelViewSet):
    queryset = StatusOrder.objects.all()
    serializer_class = StatusOrderSerializer

class StatusOrderDetail(viewsets.ModelViewSet):
    queryset = StatusOrder.objects.all()
    serializer_class = StatusOrderSerializer

class StatusOrderCreate(viewsets.ModelViewSet):
    queryset = StatusOrder.objects.all()
    serializer_class = StatusOrderSerializer

