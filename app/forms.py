from django import forms
from .models import *

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'numportas', 'ano', 'codmarca', 'cor', 'valor']

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'codcargo', 'salario', 'dataadmissao']
        
class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['idveiculo', 'codservico', 'valorservico', 'dataservico']

