from django.contrib import admin

from django.contrib import admin
from .models import LineItem,Order

# Register your models here.


admin.site.register(Order)
admin.site.register(LineItem)
