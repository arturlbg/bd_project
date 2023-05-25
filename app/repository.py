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
            values = "modelo = '{}', numportas = '{}', ano = '{}', codmarca = '{}', cor = '{}', valor = {}".format(data["modelo"], data["numportas"], data["ano"],
                                                                                                                    data["codmarca"], data["cor"], data["valor"])
            query = "UPDATE public.veiculo SET {} WHERE idVeiculo = {}".format(values, data["idveiculo"]) 
            cursor.execute(query)

    def delete(self, id):
        with connection.cursor() as cursor:
            query = "DELETE FROM public.veiculo WHERE idVeiculo = %s"
            cursor.execute(query, [id])

    def getModeloFrequente(self):
        with connection.cursor() as cursor:
            query = "SELECT modelo, COUNT(*) AS quantidade FROM public.veiculo GROUP BY modelo ORDER BY quantidade DESC LIMIT 1;"
            cursor.execute(query)
            result = cursor.fetchone()
        return result
    
    def getValorTotal(self):
        with connection.cursor() as cursor:
            query = "SELECT SUM(valor) AS soma_total FROM public.veiculo;"
            cursor.execute(query)
            result = cursor.fetchone()
        return result
    
    def findByModelo(self, modelo):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.veiculo WHERE LOWER(modelo) = LOWER('{}')".format(modelo)

            cursor.execute(query)
            result = cursor.fetchall()

        return result
    

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
    
    def create(self, modelo):
        with connection.cursor() as cursor:
            data = modelo.cleaned_data
    
            data["ehflamengo"] = 'true' if data["ehflamengo"] else 'false'
            data["ehotaku"] = 'true' if data["ehotaku"] else 'false'
            data["ehsousa"] = 'true' if data["ehsousa"] else 'false'
            
            values = "'{}', '{}', '{}', '{}', '{}', {}, {}".format(data["nome"], data["endereco"], data["telefone"], data["email"], data["ehflamengo"], data["ehotaku"], data["ehsousa"])
            query = "INSERT INTO public.cliente (nome, endereco, telefone, email, ehflamengo, ehotaku, ehsousa) VALUES (" + values + ")" 
            cursor.execute(query)
    
    def findByNome(self, nome):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.cliente WHERE LOWER(nome) LIKE LOWER('%{}%')".format(nome)

            cursor.execute(query)
            result = cursor.fetchall()

        return result
    
    def update(self, modelo):
        with connection.cursor() as cursor:
            data = modelo.cleaned_data
            values = "nome = '{}', endereco = '{}', telefone = '{}', email = '{}', ehflamengo = {}, ehotaku = {}, ehsousa = {}".format(data["nome"], data["endereco"], data["telefone"],
                                                                                                                    data["email"], data["ehflamengo"], data["ehotaku"], data["ehsousa"])
            query = "UPDATE public.cliente SET {} WHERE idCliente = {}".format(values, data["idcliente"]) 
            cursor.execute(query)

    def getTotalFlamenguistas(self):
        with connection.cursor() as cursor:
            query = "SELECT COUNT(*) AS total_flamengo FROM public.cliente WHERE ehflamengo = 'true';"
            cursor.execute(query)
            result = cursor.fetchone()
        return result

    def getTotalOtakus(self):
        with connection.cursor() as cursor:
            query = "SELECT COUNT(*) AS total_otaku FROM public.cliente WHERE ehotaku = 'true';"
            cursor.execute(query)
            result = cursor.fetchone()
        return result
    
    def getTotalSousa(self):
        with connection.cursor() as cursor:
            query = "SELECT COUNT(*) AS total_sousa FROM public.cliente WHERE ehsousa = 'true';"
            cursor.execute(query)
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
    
    def delete(self, id):
        with connection.cursor() as cursor:
            query = "DELETE FROM public.funcionario WHERE idFuncionario = %s"
            cursor.execute(query, [id])
    
    def create(self, modelo):
        with connection.cursor() as cursor:
            data = modelo.cleaned_data
            values = "'{}', '{}', '{}', '{}'".format(data["nome"], data["codcargo"], data["salario"], data["dataadmissao"])
            query = "INSERT INTO public.funcionario (nome, codcargo, salario, dataadmissao) VALUES (" + values + ")" 
            cursor.execute(query)

    def update(self, modelo):
        with connection.cursor() as cursor:
            data = modelo.cleaned_data
            values = "nome = '{}', codcargo = '{}', salario = '{}', dataadmissao = '{}'".format(data["nome"], data["codcargo"], data["salario"],
                                                                                                                    data["dataadmissao"])
            query = "UPDATE public.funcionario SET {} WHERE idFuncionario = {}".format(values, data["idfuncionario"]) 
            cursor.execute(query)
    
    def getMaiorSalario(self):
        with connection.cursor() as cursor:
            query = "SELECT MAX(salario) AS maior_salario FROM public.funcionario;"
            cursor.execute(query)
            result = cursor.fetchone()
        return result
    
    def getTotalSalario(self):
        with connection.cursor() as cursor:
            query = query = "SELECT SUM(salario) AS salario_total FROM public.funcionario;"
            cursor.execute(query)
            result = cursor.fetchone()
        return result

    def findByNome(self, nome):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.funcionario WHERE LOWER(nome) LIKE LOWER('%{}%')".format(nome)

            cursor.execute(query)
            result = cursor.fetchall()

        return result

    
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

class VendaRepository:
    def findAll(self):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.venda"
            cursor.execute(query)
            results = cursor.fetchall()
        return results

    def findById(self, id):
        with connection.cursor() as cursor:
            query = "SELECT * FROM public.venda WHERE idVenda = %s"
            cursor.execute(query, [id])
            result = cursor.fetchone()
        return result
    
    def create(self, modelo):
        with connection.cursor() as cursor:
            data = modelo.cleaned_data
            values = "'{}', '{}', '{}', {}".format(data["idveiculo"].idveiculo, data["idcliente"].idcliente, data["datavenda"], data["valorvenda"])
            query = "INSERT INTO public.venda (idveiculo, idcliente, datavenda, valorvenda) VALUES (" + values + ")" 
            cursor.execute(query)

    def update(self, modelo):
        with connection.cursor() as cursor:
            data = modelo.cleaned_data
            values = "idveiculo = '{}', idcliente = '{}', datavenda = '{}', valorvenda = '{}'".format(data["idveiculo"].idveiculo, data["idcliente"].idcliente, data["datavenda"], data["valorvenda"])
            query = "UPDATE public.venda SET {} WHERE idVenda = {}".format(values, data["idvenda"]) 
            print(query)
            cursor.execute(query)
    def delete(self, id):
        with connection.cursor() as cursor:
            query = "DELETE FROM public.venda WHERE idVenda = %s"
            print(query)
            cursor.execute(query, [id])

    def getTotalValorVenda(self):
        with connection.cursor() as cursor:
            query = query = "SELECT SUM(valorvenda) AS venda_total FROM public.venda;"
            cursor.execute(query)
            result = cursor.fetchone()
        return result