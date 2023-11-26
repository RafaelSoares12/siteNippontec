from django.contrib import admin

from main.models import Contato, Contrato, InicioSection, RedeSocial

@admin.register(InicioSection)
class InicioSectionAdmin(admin.ModelAdmin):
   ...      

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    ...

@admin.register(RedeSocial)
class RedesSociaisAdmin(admin.ModelAdmin):
   ...    

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
   ...    
