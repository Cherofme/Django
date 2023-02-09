from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'weight', 'name_tag', 'price',
    )
    search_fields = ['weight', 'name_tag', 'price']