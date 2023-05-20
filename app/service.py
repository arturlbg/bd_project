from .repository import StudentRepository
from .utils import convert_to_json

class StudentService:
    def findAll(self):
        repository = StudentRepository()
        obj = repository.findAll()
        json = convert_to_json.convert_to_json(['id', 'name', 'des'], obj)
        return json

    def findById(self, id):
        repository = StudentRepository()
        obj = repository.findById(id)
        return obj
