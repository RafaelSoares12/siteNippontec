from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(
        label="Nome",
        widget=forms.TextInput(attrs={"class": "mt-1 p-2 border border-gray-300 rounded-md w-full"}),
        required=True
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={"class": "mt-1 p-2 border border-gray-300 rounded-md w-full"}),
        required=True
    )
    assunto = forms.ChoiceField(
        label="Assunto",
        choices=[("", "Selecione um assunto"), ("Suporte", "Suporte"), ("Vendas", "Vendas"), ("Feedback", "Feedback")],
        widget=forms.Select(attrs={"class": "mt-1 p-2 border border-gray-300 rounded-md w-full"}),
        required=True
    )
    mensagem = forms.CharField(
        label="Mensagem",
        widget=forms.Textarea(attrs={"class": "mt-1 p-2 border border-gray-300 rounded-md w-full", "rows": 4}),
        required=True,
        max_length=500
    )
