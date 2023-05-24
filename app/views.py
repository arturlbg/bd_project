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
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.cleaned_data['idveiculo'] = id
            service = VeiculoService()
            service.update(form)
        
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

def funcionario(request):
    service = FuncionarioService()
    obj = service.findAll()
    obj = json.loads(obj)
    context = {
        "obj": obj,
    }
    return render(request, "Funcionario/index.html", context)

def get_funcionario(request, id):
    service = FuncionarioService()
    obj = service.findById(id)
    context = {
        "obj": obj,
    }
    return render(request, 'Funcionario/edit.html', context)

def novo_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            print(form.fields.keys())
            print(form.cleaned_data)
            service = FuncionarioService()
            service.create(form)
    else:
        form = FuncionarioForm()

    return render(request, 'Funcionario/new.html')