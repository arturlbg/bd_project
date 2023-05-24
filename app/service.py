from .repository import *
from .utils import convert_to_json
import json
from datetime import date

class VeiculoService:
    def findAll(self):
        repository = VeiculoRepository()
        obj = repository.findAll()
        json = convert_to_json.convert_to_json(['idveiculo', 'valor', 'codmarca',
                                                'numportas', 'ano', 'modelo', 'cor'], obj)
        return json

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
                'codcargo': item[2],
                'salario': item[3],
                'dataadmissao': item[4].strftime('%Y-%m-%d')
            }
            obj_modified.append(item_dict)
        json_data = json.dumps(obj_modified)
        return json_data
        '''
        json = convert_to_json.convert_to_json(['idfuncionario', 'nome', 'codcargo',
                                                'salario', 'dataadmissao'], obj)
        return json
        '''
