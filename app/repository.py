from django.db import connection

class VeiculoRepository:
    def findAll(self):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.veiculo"
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    def findById(self, id):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.veiculo WHERE idVeiculo = %s"
            cursor.execute(query, [id])
            result = cursor.fetchone()
        return result
    
    def create(self, modelo):
        with connection.cursor() as cursor:
            data = modelo.cleaned_data
            values = "'{}', '{}', '{}', '{}', '{}', {}".format(data["modelo"], data["numportas"], data["ano"], data["codmarca"], data["cor"], data["valor"])
            query = "INSERT INTO public.veiculo (modelo, numportas, ano, codmarca, cor, valor) VALUES (" + values + ")" 
            cursor.execute(query)

    def update(self, modelo):
        with connection.cursor() as cursor:
            data = modelo.cleaned_data
            print(data)
            values = "modelo = '{}', numportas = '{}', ano = '{}', codmarca = '{}', cor = '{}', valor = {}".format(data["modelo"], data["numportas"], data["ano"],
                                                                                                                    data["codmarca"], data["cor"], data["valor"])
            query = "UPDATE public.veiculo SET {} WHERE idVeiculo = {}".format(values, data["idveiculo"]) 
            cursor.execute(query)

class ClienteRepository:
    def findAll(self):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.cliente"
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    def findById(self, id):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.cliente WHERE idCliente = %s"
            cursor.execute(query, [id])
            result = cursor.fetchone()
        return result
    
class FuncionarioRepository:
    def findAll(self):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.funcionario"
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    def findById(self, id):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.funcionario WHERE idFuncionario = %s"
            cursor.execute(query, [id])
            result = cursor.fetchone()
        return result
    
    def create(self, modelo):
        with connection.cursor() as cursor:
            data = modelo.cleaned_data
            values = "'{}', '{}', '{}', '{}'".format(data["nome"], data["codcargo"], data["salario"], data["dataadmissao"])
            query = "INSERT INTO public.funcionario (nome, codcargo, salario, dataadmissao) VALUES (" + values + ")" 
            cursor.execute(query)

    
class ServicoRepository:
    def findAll(self):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.servico"
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    def findById(self, id):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.servico WHERE idServico = %s"
            cursor.execute(query, [id])
            result = cursor.fetchone()
        return result
    
    def create(self, modelo):
        with connection.cursor() as cursor:
            data = modelo.cleaned_data
            values = "'{}', '{}', '{}', '{}'".format(data["idveiculo"].idveiculo, data["codservico"], data["valorservico"], data["dataservico"])
            query = "INSERT INTO public.servico (idveiculo, codservico, valorservico, dataservico) VALUES (" + values + ")" 
            cursor.execute(query)