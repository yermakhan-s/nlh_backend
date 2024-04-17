from django.contrib import admin
from .models import ItemCategory, Item

# Register your models here.
@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
