from django.contrib import admin
from .models import Panier, PanierItem

# Register your models here.

admin.site.register(Panier)
admin.site.register(PanierItem)