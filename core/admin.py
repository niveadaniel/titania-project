from django.contrib import admin
from .models import Owner, OwnerContractType, OwnerSituation, Tower, VehicleType, Notification


@admin.register(Owner)
class Owner(admin.ModelAdmin):
    list_display = ['id', 'name', 'tower', 'apartment']
    search_fields = ['id', 'name', 'tower', 'apartment']


@admin.register(OwnerContractType)
class OwnerContractType(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(OwnerSituation)
class OwnerSituation(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Tower)
class Tower(admin.ModelAdmin):
    list_display = ['id', 'number']
    search_fields = ['id', 'number']


@admin.register(VehicleType)
class VehicleType(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['id', 'name']


@admin.register(Notification)
class Notification(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    search_fields = ['id', 'title', 'author']
