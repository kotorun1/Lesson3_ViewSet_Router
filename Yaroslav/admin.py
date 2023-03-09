from django.contrib import admin

# Register your models here.
from .models import Pet, Order, Category, StatusPet, Type, StatusOrder

admin.site.register(Pet)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(StatusPet)
admin.site.register(Type)
admin.site.register(StatusOrder)
