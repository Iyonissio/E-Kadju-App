from django.contrib import admin

# Register your models here.

from .models import Categoria, Sub_Categoria, Producto, Contact_us

admin.site.register(Categoria)
admin.site.register(Sub_Categoria)
admin.site.register(Producto)
admin.site.register(Contact_us)