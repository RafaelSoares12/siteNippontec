from django.views.generic import TemplateView
from main.forms import ContatoForm

from main.models import Contato, RedeSocial

class ContatoTemplateView(TemplateView):
    template_name = 'contato.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contatoForm'] = ContatoForm()
        context["contato"] = Contato.objects.get(id=1)
        context["redesSociais"] = RedeSocial.objects.all()
        return context
