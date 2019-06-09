from django.contrib import admin
from .models import Product
# Register your models here.


# display the apps in admin pannel

admin.site.register(Product)
