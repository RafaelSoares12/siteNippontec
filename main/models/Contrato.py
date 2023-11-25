from django.db import models

class Contrato(models.Model):
    nome = models.CharField('Nome do Contrato', max_length=255)
    documento = models.FileField('Faça upload do contrato', upload_to='contratos/')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"