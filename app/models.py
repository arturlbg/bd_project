from django.db import models


class Marca(models.Model):
    codmarca = models.AutoField(primary_key=True, null=False)
    nomemarca = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nomemarca
    
    class Meta:
        db_table = "marca"

class Cargo(models.Model):
    codcargo = models.AutoField(primary_key=True, null=False)
    nomecargo = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nomecargo
    
    class Meta:
        db_table = "cargo"

class Veiculo(models.Model):
    idveiculo = models.AutoField(primary_key=True, null=False)
    codmarca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=False)
    valor = models.DecimalField(max_digits=7, decimal_places=2, null=False)
    numportas = models.CharField(max_length=1, null=False)
    ano = models.CharField(max_length=4, null=False)
    modelo = models.CharField(max_length=30, null=False)
    cor = models.CharField(max_length=20, null=False)
    statusvenda = models.BooleanField(null=False)

    def __str__(self):
         return self.modelo
     
    class Meta:
         db_table = "veiculo"

class Funcionario(models.Model):
    idfuncionario = models.AutoField(primary_key=True, null=False)
    nome = models.CharField(max_length=100, null=False)
    codcargo = models.CharField(max_length=20, null=False)
    salario = models.DecimalField(max_digits=7, decimal_places=2, null=False)
    dataadmissao = models.DateField(max_length=10, null=False)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = "funcionario"

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True, null=False)
    nome = models.CharField(max_length=100, null=False)
    endereco = models.CharField(max_length=100, null=False)
    telefone = models.CharField(max_length=14, null=False)
    email = models.CharField(max_length=50, null=False)
    ehflamengo = models.BooleanField(null=False)
    ehotaku = models.BooleanField(null=False)
    ehsousa = models.BooleanField(null=False)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = "cliente"

class Pagamento(models.Model):
    codpagamento = models.AutoField(primary_key=True, null=False)
    tipopgto = models.CharField(max_length=30, null=False)
    statusConfirmacao = models.BooleanField(null=False)

    def __str__(self):
        return self.tipopgto
    
    class Meta:
        db_table = "pagamento"

class Venda(models.Model):
    idvenda = models.AutoField(primary_key=True, null=False)
    idveiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, null=False)
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
    idfuncionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, null=False)
    codpagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE, null=False)
    datavenda = models.DateField(max_length=10, null=False)
    valorvenda = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    
    def __str__(self):
        return self.idvenda
    
    class Meta:
        db_table = "venda"