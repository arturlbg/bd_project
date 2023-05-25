from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'telefone', 'email', 'ehflamengo', 'ehotaku', 'ehsousa']
        
class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'codcargo', 'salario', 'dataadmissao']

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['modelo', 'numportas', 'ano', 'codmarca', 'cor', 'valor']
        
class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['idveiculo', 'codservico', 'valorservico', 'dataservico']

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['idveiculo', 'idcliente', 'datavenda', 'valorvenda']

