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

def edit_veiculo(request, id):
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

def delete_veiculo(request, id):
    service = VeiculoService()
    if request.method == 'DELETE':
        service.delete(id)
    
    obj = service.findAll()
    obj = json.loads(obj)
    context = {
        "obj": obj,
    }
    return render(request, 'Veiculo/index.html', context)

def search_veiculo(request, modelo):
    service = VeiculoService()
    obj = service.findByModelo(modelo)
    obj = json.loads(obj)

    context = {
        "obj": obj,
    }
    return render(request, 'Veiculo/search.html', context)

def novo_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            service = VeiculoService()
            service.create(form)

    return render(request, 'Veiculo/new.html')

def cliente(request):
    service = ClienteService()
    obj = service.findAll()
    obj = json.loads(obj)
    context = {
        "obj": obj,
    }
    return render(request, "Cliente/index.html", context)

def novo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            service = ClienteService()
            service.create(form)

    return render(request, 'Cliente/new.html')

def edit_cliente(request, id):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.cleaned_data['idcliente'] = id
            service = ClienteService()
            service.update(form)
        
    service = ClienteService()
    obj = service.findById(id)
    context = {
        "obj": obj,
    }
    return render(request, 'Cliente/edit.html', context)

def search_cliente(request, nome):
    service = ClienteService()
    obj = service.findByNome(nome)
    obj = json.loads(obj)

    context = {
        "obj": obj,
    }
    return render(request, 'Cliente/search.html', context)

def funcionario(request):
    service = FuncionarioService()
    obj = service.findAll()
    obj = json.loads(obj)
    context = {
        "obj": obj,
    }
    return render(request, "Funcionario/index.html", context)

def edit_funcionario(request, id):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.cleaned_data['idfuncionario'] = id
            service = FuncionarioService()
            service.update(form)
            
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
            service = FuncionarioService()
            service.create(form)
    
    return render(request, 'Funcionario/new.html')

def delete_funcionario(request, id):
    service = FuncionarioService()
    if request.method == 'DELETE':
        service.delete(id)
    
    obj = service.findAll()
    obj = json.loads(obj)
    context = {
        "obj": obj,
    }
    return render(request, 'Funcionario/index.html', context)

def search_funcionario(request, nome):
    service = FuncionarioService()
    obj = service.findByNome(nome)
    obj = json.loads(obj)

    context = {
        "obj": obj,
    }
    return render(request, 'Funcionario/search.html', context)

def novo_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            service = ServicoService()
            service.create(form)

    veiculo_service = VeiculoService()
    veiculo = json.loads(veiculo_service.findAll())
    context = {
        "veiculo": veiculo
    }
    return render(request, 'Servico/new.html', context)