from django.shortcuts import render
from .service import *
from .forms import *
import json


########################################################################VEICULO########################################################################
def veiculo(request):
    service = VeiculoService()
    obj = service.findAll()
    obj = json.loads(obj)

    for veiculo in obj:
        marca = Marca.objects.get(codmarca=veiculo['codmarca'])
        veiculo['nomemarca'] = marca.nomemarca

    modeloFrequente = service.getModeloFrequente()
    valorTotal = service.getValorTotal()

    context = {
        "obj": obj,
        "modeloFrequente": modeloFrequente,
        "valorTotal": valorTotal
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

            codmarca_nome = request.POST.get('codmarca')  
            marca = Marca.objects.get(nomemarca=codmarca_nome) 
            form.instance.codmarca = marca 

            service.create(form)

    marca_service = MarcaService()
    marcas = json.loads(marca_service.findAll())

    context = {
        "marcas": marcas,
    }
    return render(request, 'Veiculo/new.html', context)

'''def novo_veiculo(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            service = VeiculoService()
            service.create(form)

    return render(request, 'Veiculo/new.html')'''

########################################################################CLIENTE########################################################################

def cliente(request):
    service = ClienteService()
    obj = service.findAll()
    obj = json.loads(obj)

    totalFlamenguistas = service.getTotalFlamenguistas()
    totalOtakus = service.getTotalOtakus()
    totalSousa = service.getTotalSousa()
    context = {
        "obj": obj,
        "totalFlamenguistas": totalFlamenguistas,
        "totalOtakus": totalOtakus,
        "totalSousa": totalSousa,
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

########################################################################FUNCIONARIO########################################################################

def funcionario(request):
    service = FuncionarioService()
    obj = service.findAll()
    obj = json.loads(obj)

    maiorSalario = service.getMaiorSalario()
    totalSalario = service.getTotalSalario()

    for funcionario in obj:
        cargo = Cargo.objects.get(codcargo=funcionario['codcargo'])
        funcionario['nomecargo'] = cargo.nomecargo

    context = {
        "obj": obj,
        "maiorSalario": maiorSalario,
        "totalSalario": totalSalario,
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

########################################################################VENDA########################################################################

def venda(request):
    service = VendaService()
    obj = service.findAll()
    obj = json.loads(obj)

    vendaTotal = service.getTotalValorVenda()
    context = {
        "obj": obj,
        "vendaTotal": vendaTotal,
    }
    return render(request, "Venda/index.html", context)

def novo_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        print(form.data)
        if form.is_valid():
            service = VendaService()
            service.create(form)

    veiculo_service = VeiculoService()
    veiculo = json.loads(veiculo_service.findAll())

    cliente_service = ClienteService()
    cliente = json.loads(cliente_service.findAll())
    context = {
        "veiculo": veiculo,
        "cliente": cliente,
    }
    return render(request, 'Venda/new.html', context)

def edit_venda(request, id):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.cleaned_data['idvenda'] = id
            service = VendaService()
            service.update(form)
        
    service = VendaService()
    obj = service.findById(id)

    veiculo_service = VeiculoService()
    veiculo = json.loads(veiculo_service.findAll())

    cliente_service = ClienteService()
    cliente = json.loads(cliente_service.findAll())
    context = {
        "obj": obj,
        "veiculo": veiculo,
        "cliente": cliente,
    }
    return render(request, 'Venda/edit.html', context)

def delete_venda(request, id):
    service = VendaService()
    if request.method == 'DELETE':
        service.delete(id)

    obj = service.findAll()
    obj = json.loads(obj)

    context = {
        "obj": obj,
    }
    return render(request, "Venda/index.html", context)