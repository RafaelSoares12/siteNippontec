from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from main.forms import ContatoForm

class EnviarMensagemView(FormView):
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('main:contatos')

    def form_valid(self, form):
        assunto = f'Site Nippontec - {form.cleaned_data["assunto"]}'
        mensagem = f"De: {form.cleaned_data['nome']} ({form.cleaned_data['email']})\n\n{form.cleaned_data['mensagem']}"

        try:
            send_mail(assunto, mensagem, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            messages.success(self.request, 'Obrigado pelo contato! Mensagem enviada com sucesso.')
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f'Ocorreu um erro ao enviar a mensagem: {e}')
            return self.form_invalid(form)
