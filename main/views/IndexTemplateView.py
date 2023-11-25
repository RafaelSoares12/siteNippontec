from django.views.generic import TemplateView

from main.models import RedeSocial

class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["redesSociais"] = RedeSocial.objects.all()
        return context