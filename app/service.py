from .repository import *
from .utils import convert_to_json
import json
from datetime import date

class VeiculoService:
    def findAll(self):
        repository = VeiculoRepository()
        obj = repository.findAll()
        obj_modified = []

        for item in obj:
            item_dict = {
                'idveiculo': item[0],
                'valor': float(item[1]),
                'numportas': item[2],
                'ano': item[3],
                'modelo': item[4],
                'cor': item[5],
                'statusvenda': item[6],
                'codmarca': item[7],
            }
            obj_modified.append(item_dict)

        json_data = json.dumps(obj_modified)
        return json_data

    def findById(self, id):
        repository = VeiculoRepository()
        obj = repository.findById(id)
        return obj
    
    def create(self, modelo):
        repository = VeiculoRepository()
        repository.create(modelo)
    
    def update(self, modelo):
        repository = VeiculoRepository()
        repository.update(modelo)

    def delete(self, id):
        repository = VeiculoRepository()
        repository.delete(id)

    def findByModelo(self, modelo):
        repository = VeiculoRepository()
        obj = repository.findByModelo(modelo)
        obj_modified = []

        for item in obj:
            item_dict = {
                'idveiculo': item[0],
                'valor': float(item[1]),
                'numportas': item[2],
                'ano': item[3],
                'modelo': item[4],
                'cor': item[5],
                'statusvenda': item[6],
                'codmarca': item[7],
            }
            obj_modified.append(item_dict)

        json_data = json.dumps(obj_modified)
        return json_data
    
    def getModeloFrequente(self):
        repository = VeiculoRepository()
        return repository.getModeloFrequente()
    
    def getValorTotal(self):
        repository = VeiculoRepository()
        return repository.getValorTotal()
    
class ClienteService:
    def findAll(self):
        repository = ClienteRepository()
        obj = repository.findAll()
        json = convert_to_json.convert_to_json(['idcliente', 'nome', 'endereco',
                                                'telefone', 'email', 'ehflamengo',
                                                'ehotaku', 'ehsousa'], obj)
        return json

    def findById(self, id):
        repository = ClienteRepository()
        obj = repository.findById(id)
        return obj
    
    def create(self, modelo):
        repository = ClienteRepository()
        repository.create(modelo)

    def update(self, modelo):
        repository = ClienteRepository()
        repository.update(modelo)
    
    def getTotalFlamenguistas(self):
        repository = ClienteRepository()
        return repository.getTotalFlamenguistas()
    
    def getTotalOtakus(self):
        repository = ClienteRepository()
        return repository.getTotalOtakus()
    
    def getTotalSousa(self):
        repository = ClienteRepository()
        return repository.getTotalSousa()

    def findByNome(self, nome):
        repository = ClienteRepository()
        obj = repository.findByNome(nome)
        json = convert_to_json.convert_to_json(['idcliente', 'nome', 'endereco',
                                                'telefone', 'email', 'ehflamengo',
                                                'ehotaku', 'ehsousa'], obj)
        return json

class FuncionarioService:
    def findAll(self):
        repository = FuncionarioRepository()
        obj = repository.findAll()
        # Converter cada tupla em um dicionário e alterar a chave 'dataadmissao' para uma string formatada
        obj_modified = []
        for item in obj:
            item_dict = {
                'idfuncionario': item[0],
                'nome': item[1],
                'salario': float(item[2]),
                'dataadmissao': item[3].strftime('%Y-%m-%d'),
                'codcargo': item[4]

            }
            obj_modified.append(item_dict)
        json_data = json.dumps(obj_modified)
        return json_data
        '''
        json = convert_to_json.convert_to_json(['idfuncionario', 'nome', 'codcargo',
                                                'salario', 'dataadmissao'], obj)
        return json
        '''
    def findById(self, id):
        repository = FuncionarioRepository()
        obj = repository.findById(id)
        return obj
    
    def create(self, modelo):
        repository = FuncionarioRepository()
        repository.create(modelo)

    def update(self, modelo):
        repository = FuncionarioRepository()
        repository.update(modelo)

    def delete(self, id):
        repository = FuncionarioRepository()
        repository.delete(id)
    
    def getMaiorSalario(self):
        repository = FuncionarioRepository()
        return repository.getMaiorSalario()

    def getTotalSalario(self):
        repository = FuncionarioRepository()
        return repository.getTotalSalario()

    def findByNome(self, nome):
        repository = FuncionarioRepository()
        obj = repository.findByNome(nome)

        obj_modified = []
        for item in obj:
            item_dict = {
                'idfuncionario': item[0],
                'nome': item[1],
                'codcargo': item[2],
                'salario': float(item[3]),
                'dataadmissao': item[4].strftime('%Y-%m-%d')
            }
            obj_modified.append(item_dict)
        json_data = json.dumps(obj_modified)
        return json_data

class VendaService:
    def findAll(self):
        repository = VendaRepository()
        obj = repository.findAll()
        obj_modified = []

        for item in obj:
            item_dict = {
                'idvenda': item[0],
                'datavenda': item[1].strftime('%Y-%m-%d'),
                'percentdesconto': float(item[2]),
                'valorvenda': float(item[3]),
                'codpagamento': item[4],
                'idcliente': item[5],
                'idfuncionario': item[6],
                'idveiculo': item[7],
            }
            obj_modified.append(item_dict)

        json_data = json.dumps(obj_modified)
        return json_data

    def findById(self, id):
        repository = VendaRepository()
        obj = repository.findById(id)
        return obj
    
    def create(self, modelo):
        repository = VendaRepository()
        repository.create(modelo)
    
    def update(self, modelo):
        repository = VendaRepository()
        repository.update(modelo)

    def delete(self, id):
        repository = VendaRepository()
        repository.delete(id)

    def getTotalValorVenda(self):
        repository = VendaRepository()
        return repository.getTotalValorVenda()
    
class MarcaService:
    def findAll(self):
        repository = MarcaRepository()
        obj = repository.findAll()
        json = convert_to_json.convert_to_json(['codmarca', 'nome'], obj)
        return json

    def findById(self, id):
        repository = MarcaRepository()
        obj = repository.findById(id)
        return obj
    
    def create(self, modelo):
        repository = MarcaRepository()
        repository.create(modelo)

    def update(self, modelo):
        repository = MarcaRepository()
        repository.update(modelo)

    def delete(self, id):
        repository = MarcaRepository()
        repository.delete(id)

    def findByNome(self, nome):
        repository = MarcaRepository()
        obj = repository.findByNome(nome)
        json = convert_to_json.convert_to_json(['codmarca', 'nome'], obj)
        return json


class PagamentoService:
    def findAll(self):
        repository = PagamentoRepository()
        obj = repository.findAll()
        json = convert_to_json.convert_to_json(['codpagamento', 'tipopgto', 'statusConfirmacao'], obj)
        return json

    def findById(self, id):
        repository = PagamentoRepository()
        obj = repository.findById(id)
        return obj
    
    def create(self, modelo):
        repository = PagamentoRepository()
        repository.create(modelo)

    def update(self, modelo):
        repository = PagamentoRepository()
        repository.update(modelo)

    def delete(self, id):
        repository = PagamentoRepository()
        repository.delete(id)

    def findByTipoPgto(self, tipoPgto):
        repository = PagamentoRepository()
        obj = repository.findByTipoPgto(tipoPgto)
        json = convert_to_json.convert_to_json(['codpagamento', 'tipopgto', 'statusConfirmacao'], obj)
        return json
    
class HistoricoVendaService:
    def findAll(self):
        repository = HistoricoVendaRepository()
        obj = repository.findAll()
        obj_modified = []

        for item in obj:
            item_dict = {
                'datavenda': item[0].strftime('%Y-%m-%d'),
                'valorvendafinal': float(item[1]),
                'modeloveiculo': item[2],
                'anoveiculo': item[3],
                'tipopagamento': item[4],
                'marcaveiculo': item[5],
                'vendedor': item[6],
                'cliente': item[6],
            }
            obj_modified.append(item_dict)

        json_data = json.dumps(obj_modified)
        return json_data