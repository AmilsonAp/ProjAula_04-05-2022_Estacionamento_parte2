from django import forms
from estacionamento.models import Locacao


class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = ['cliente', 'carro', 'funcionario', 'dataLocacao', 'valor', 'dataDevolucao']
