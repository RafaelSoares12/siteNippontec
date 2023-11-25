from django.views.generic import TemplateView

from main.models import Contrato

class ContratoTemplateView(TemplateView):
    template_name = 'contratos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contratos"] = Contrato.objects.all()
        return context
