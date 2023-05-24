from django.db import models

# Create your models here.
class Veiculo(models.Model):
    idveiculo = models.AutoField(primary_key=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    codmarca = models.CharField(max_length=20)
    numportas = models.CharField(max_length=1)
    ano = models.CharField(max_length=4)
    modelo = models.CharField(max_length=30)
    cor = models.CharField(max_length=20)

    def __str__(self):
         return self.modelo
     
    class Meta:
         db_table = "veiculo"

class Servico(models.Model):
    idservico = models.AutoField(primary_key=True)
    idveiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    codservico = models.CharField(max_length=20)
    valorservico = models.DecimalField(max_digits=7, decimal_places=2)
    dataservico = models.DateField(max_length=10)
    
    def __str__(self):
        return self.codservico
    
    class Meta:
        db_table = "servico"

class Funcionario(models.Model):
    idfuncionario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    codcargo = models.CharField(max_length=20)
    salario = models.DecimalField(max_digits=7, decimal_places=2)
    dataadmissao = models.DateField(max_length=10)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = "funcionario"

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    ehflamengo = models.BooleanField()
    ehotaku = models.BooleanField()
    ehsousa = models.BooleanField()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = "cliente"

class Agendamento(models.Model):
    idagendamento = models.AutoField(primary_key=True)
    idveiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    codservico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    dataagendamento = models.DateField()
    
    def __str__(self):
        return self.idagendamento
    
    class Meta:
        db_table = "agendamento"

class Venda(models.Model):
    idvenda = models.AutoField(primary_key=True)
    idveiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    datavenda = models.DateField(max_length=10)
    valorvenda = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self):
        return self.idvenda
    
    class Meta:
        db_table = "venda"