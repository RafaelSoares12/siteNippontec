from django.urls import path

from main.views import ContatoTemplateView, ContratoTemplateView, IndexTemplateView, EnviarMensagemView

app_name='main'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('contatos/', ContatoTemplateView.as_view(), name='contatos'),
    path('contratos/', ContratoTemplateView.as_view(), name='contratos'),
    path('enviar-mensagem', EnviarMensagemView.as_view(), name='enviar-mensagem')
]