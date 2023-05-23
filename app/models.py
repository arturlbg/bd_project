from django.db import models

class Veiculo(models.Model):
    idVeiculo = models.AutoField(primary_key=True)
    valor = models.FloatField()
    codMarca = models.CharField(max_length=20)
    numPortas = models.CharField(max_length=1)
    ano = models.CharField(max_length=4)
    modelo = models.CharField(max_length=30)
    cor = models.CharField(max_length=20)
    def __str__(self):
        return self.modelo
    
    class Meta:
        db_table = "Veiculo"

class Servico(models.Model):
    idServico = models.AutoField(primary_key=True)
    idVeiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    codServico = models.CharField(max_length=20)
    valorServico = models.FloatField()
    dataServico = models.DateField()
    
    def __str__(self):
        return self.codServico
    
    class Meta:
        db_table = "Servico"

class Funcionario(models.Model):
    idFuncionario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    codCargo = models.CharField(max_length=20)
    salario = models.FloatField()
    dataAdmissao = models.DateField()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = "Funcionario"

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    ehFlamengo = models.BooleanField()
    ehOtaku = models.BooleanField()
    ehSousa = models.BooleanField()
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = "Cliente"

class Agendamento(models.Model):
    idAgendamento = models.AutoField(primary_key=True)
    idVeiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    codServico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    dataAgendamento = models.DateField()
    
    def __str__(self):
        return self.idAgendamento
    
    class Meta:
        db_table = "Agendamento"

class Venda(models.Model):
    idVenda = models.AutoField(primary_key=True)
    idVeiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    dataVenda = models.DateField()
    valorVenda = models.FloatField()
    
    def __str__(self):
        return self.idVenda
    
    class Meta:
        db_table = "Venda"