from django.db import models

class Contato(models.Model):
    tituloPrincipal = models.CharField('Título Principal', max_length=35)
    mensagem = models.CharField('Mensagem', max_length=200)    
    telefone = models.CharField('Telefone', max_length=20)
    endereco = models.CharField('Endereço', max_length=255)
    telefone = models.CharField('Telefone', max_length=20)
    email = models.EmailField('Email')

    def __str__(self):
        return 'Página de contatos'
    
    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contato"