from django.db import models

class RedesSociais(models.Model):
    nome = models.CharField('Nome da rede social', max_length=25)
    link = models.URLField('Link', max_length=200)
    icone = models.CharField('Ícone', max_length=250)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Rede Social"
        verbose_name_plural = "Redes Sociais"
