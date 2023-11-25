from django.contrib import admin

from main.models import Contrato, InicioSection, RedeSocial

@admin.register(InicioSection)
class InicioSectionAdmin(admin.ModelAdmin):
   ...      

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    ...

@admin.register(RedeSocial)
class RedesSociaisAdmin(admin.ModelAdmin):
   ...    

