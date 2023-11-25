from django.db import models

class InicioSection(models.Model):
    title = models.CharField('Texto principal', max_length=100)
    subtitle = models.CharField('Subtítulo', max_length=100)
    buttonText = models.CharField('Texto do botão', max_length=50)
    buttonLink = models.CharField('Link do botão', max_length=100)
    backgroundImage = models.ImageField('Imagem de fundo', upload_to='inicioBackgrounds/')
    image = models.ImageField('Imagem modelo' ,upload_to='inicioImages/')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Seção Início"
        verbose_name_plural = "Seção Início"

    