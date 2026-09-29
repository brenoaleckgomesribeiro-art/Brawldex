from django import forms
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