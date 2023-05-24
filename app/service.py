from .repository import *
from .utils import convert_to_json

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
    
class ServicoService:
    def findById(self, id):
        repository = ServicoRepository()
        obj = repository.findById(id)
        return obj

    def create(self, modelo):
        repository = ServicoRepository()
        repository.create(modelo)
