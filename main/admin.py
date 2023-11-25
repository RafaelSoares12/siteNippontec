from django.contrib import admin

from main.models import Contrato, RedesSociais

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    ...

@admin.register(RedesSociais)
class RedesSociaisAdmin(admin.ModelAdmin):
   ...    