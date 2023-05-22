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