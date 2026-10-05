from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Brawler


class BrawlerForm(forms.ModelForm):
    class Meta:
        model = Brawler
        fields = [
            'nome',
            'raridade',
            'classe',
            'vida',
            'dano',
            'descricao',
            'imagem',
        ]


class CadastroForm(UserCreationForm):
    """
    Formulário de cadastro de usuário.
    Usa o UserCreationForm do Django (usuário + senha + confirmação)
    e adiciona email opcional.
    """

    email = forms.EmailField(
        required=False,
        label='Email',
        help_text='Opcional.'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Adiciona classes Bootstrap em todos os campos
        for campo in self.fields.values():
            campo.widget.attrs.update({
                'class': 'form-control',
            })


class PerfilForm(forms.ModelForm):
    """
    Formulário pra editar dados da conta: nome, sobrenome, email.
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for campo in self.fields.values():
            campo.widget.attrs.update({
                'class': 'form-control',
            })