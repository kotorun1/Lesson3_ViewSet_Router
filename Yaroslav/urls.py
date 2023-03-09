from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import PetList, PetDetail, PetCreate, OrderList, OrderDetail, OrderCreate, CategoryList, CategoryDetail, CategoryCreate, StatusPetList, StatusPetDetail, StatusPetCreate, TypeList, TypeDetail, TypeCreate, StatusOrderList, StatusOrderDetail, StatusOrderCreate

router = routers.DefaultRouter()
router.register(r'pet', PetList)
router.register(r'pet', PetDetail)
router.register(r'pet', PetCreate)
router.register(r'order', OrderList)
router.register(r'order', OrderDetail)
router.register(r'order', OrderCreate)
router.register(r'category', CategoryList)
router.register(r'category', CategoryDetail)
router.register(r'category', CategoryCreate)
router.register(r'statuspet', StatusPetList)
router.register(r'statuspet', StatusPetDetail)
router.register(r'statuspet', StatusPetCreate)
router.register(r'type', TypeList)
router.register(r'type', TypeDetail)
router.register(r'type', TypeCreate)
router.register(r'statusorder', StatusOrderList)
router.register(r'statusorder', StatusOrderDetail)
router.register(r'statusorder', StatusOrderCreate)

urlpatterns = [
    path('', include(router.urls)), 
]
