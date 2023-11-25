from django.contrib import admin

from main.models import Contrato, RedeSocial

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    ...

@admin.register(RedeSocial)
class RedesSociaisAdmin(admin.ModelAdmin):
   ...    