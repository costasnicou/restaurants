from django.contrib import admin
from .models import Item,Restaurant,ItemCategory
# Register your models here.

admin.site.register(Item)
admin.site.register(Restaurant)
admin.site.register(ItemCategory)