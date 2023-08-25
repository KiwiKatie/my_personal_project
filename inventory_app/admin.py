from django.contrib import admin

from .models import Inventory, Item

admin.site.register([Inventory, Item])
