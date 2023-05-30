from django.contrib import admin
from .models import Cliente, Estoque

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Estoque)