from django import forms
from .models import Veiculo, Servico

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'numportas', 'ano', 'codmarca', 'cor', 'valor']

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['idveiculo', 'codservico', 'valorservico', 'dataservico']

