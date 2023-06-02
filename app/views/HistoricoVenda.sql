CREATE VIEW HistoricoVenda AS
SELECT venda.datavenda as DataVenda, venda.valorvenda  - (venda.valorvenda * (venda.percentdesconto/100)) as ValorVendaFinal,
veiculo.modelo as ModeloVeiculo, veiculo.ano as AnoVeiculo, pagamento.tipopgto as TipoPagamento, marca.nomemarca as MarcaVeiculo,
funcionario.nome as Vendedor, cliente.nome as Cliente
FROM public.venda venda INNER JOIN public.veiculo veiculo ON venda.idveiculo_id = veiculo.idveiculo
INNER JOIN public.pagamento pagamento ON venda.codpagamento_id = pagamento.codpagamento 
INNER JOIN public.funcionario funcionario ON venda.idfuncionario_id = funcionario.idfuncionario
INNER JOIN public.marca marca ON veiculo.codmarca_id = marca.codmarca
INNER JOIN public.cliente cliente ON venda.idcliente_id = cliente.idcliente WHERE veiculo.statusvenda = 'true';