from django.shortcuts import render
from .service import *
from .forms import *
from .models import Veiculo
import json

def veiculo(request):
    service = VeiculoService()
    obj = service.findAll()
    obj = json.loads(obj)
    context = {
        "obj": obj,
    }
    return render(request, "Veiculo/index.html", context)

def get_veiculo(request, id):
    service = VeiculoService()
    obj = service.findById(id)
    context = {
        "obj": obj,
    }
    return render(request, 'Veiculo/edit.html', context)

def novo_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            print(form.fields.keys())
            print(form.cleaned_data)
            service = VeiculoService()
            service.create(form)
    else:
        form = VeiculoForm()

    return render(request, 'Veiculo/new.html')

def cliente(request):
    service = ClienteService()
    obj = service.findAll()
    obj = json.loads(obj)
    context = {
        "obj": obj,
    }
    return render(request, "Cliente/index.html", context)

