"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/', cliente, name="cliente"),
    path('cliente/novo/', novo_cliente, name="novo_cliente"),
    path('cliente/edit/<int:id>', edit_cliente, name='edit_cliente'),
    path('funcionario/', funcionario, name="funcionario"),
    path('funcionario/novo/', novo_funcionario, name="novo_funcionario"),
    path('funcionario/edit/<int:id>', edit_funcionario, name='edit_funcionario'),
    path('veiculo/', veiculo, name="veiculo"),
    path('veiculo/novo/', novo_veiculo, name="novo_veiculo"),
    path('veiculo/edit/<int:id>', edit_veiculo, name='edit_veiculo'),
    path('veiculo/delete/<int:id>', delete_veiculo, name='delete_veiculo'),
    path('venda/', venda, name="venda"),
    path('venda/novo/', novo_venda, name="novo_venda"),
    path('venda/edit/<int:id>', edit_venda, name='edit_venda'),
    path('venda/delete/<int:id>', delete_venda, name='delete_venda'),
    path('servico/novo', novo_servico, name="novo_servico"),
]