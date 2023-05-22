from django.db import models

# Create your models here.
class Veiculo(models.Model):
    idveiculo = models.AutoField(primary_key=True)
    valor=models.FloatField()
    codmarca=models.CharField(max_length=20)
    numportas=models.CharField(max_length=1)
    ano=models.CharField(max_length=4)
    modelo=models.CharField(max_length=30)
    cor=models.CharField(max_length=20)
    def __str__(self):
        return self.modelo
    
    class Meta:
        db_table = "veiculo"