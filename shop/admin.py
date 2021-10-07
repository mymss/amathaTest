from django.contrib import admin
from .models import Produit, Prix, Atelier, Commande, LigneProduitCommande, LigneAtelierCommande
from .models import ProduitInterieur
from .models import Cosmetique
from .models import Vetement

# Register your models here.

admin.site.register(Produit)
admin.site.register(ProduitInterieur)
admin.site.register(Cosmetique)
admin.site.register(Vetement)
admin.site.register(Prix)
admin.site.register(Atelier)
admin.site.register(Commande)
admin.site.register(LigneProduitCommande)
admin.site.register(LigneAtelierCommande)

