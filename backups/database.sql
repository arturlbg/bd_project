DELETE FROM veiculo WHERE idveiculo>=1;
DELETE FROM cliente WHERE idcliente>=1;
DELETE FROM funcionario WHERE idfuncionario>=1;
DELETE FROM marca WHERE codmarca >=1;
DELETE FROM cargo WHERE codcargo >=1;

SELECT * FROM veiculo;
SELECT * FROM cliente;
SELECT * FROM funcionario;
SELECT * FROM marca;
SELECT * FROM cargo;

INSERT INTO marca (codmarca, nomemarca)
VALUES
    (1, 'Honda'),
    (2, 'Toyota'),
    (3, 'Hyundai'),
    (4, 'Nissan'),
    (5, 'Volkswagen');

INSERT INTO cargo (codcargo, nomecargo)
VALUES
    (1, 'Vendedor'),
    (2, 'Gerente'),
    (3, 'Diretor');

INSERT INTO veiculo (idveiculo, modelo, codmarca_id, numportas, ano, cor, valor, statusvenda)
VALUES
    (10, 'Civic', 1, 4, 2021, 'Preto', 75000, false),
    (11, 'Accord', 1, 4, 2022, 'Branco', 80000, false),
    (12, 'City', 3, 4, 2020, 'Vermelho', 70000, false),
    (13, 'Fit', 2, 4, 2021, 'Azul', 78000, false),
    (14, 'CR-V', 4, 4, 2023, 'Prata', 85000, false),
    (15, 'HR-V', 5, 4, 2022, 'Cinza', 77000, false),
    (16, 'Civic Type R', 5, 4, 2022, 'Amarelo', 78000, false),
    (17, 'Pilot', 1, 4, 2020, 'Verde', 74000, false),
    (18, 'Odyssey', 1, 4, 2021, 'Laranja', 76000, false),
    (19, 'Ridgeline', 2, 4, 2023, 'Roxo', 82000, false);

INSERT INTO funcionario (idfuncionario, nome, codcargo_id, salario, dataadmissao)
VALUES
    (10, 'Ronaldinho Gaúcho', 3, 9999, '2002-06-30'),
    (11, 'Roberto Carlos', 2, 5700, '2002-06-30'),
    (12, 'Ronaldo', 1, 2100, '2002-06-30'),
    (13, 'Rivaldo', 1, 2100, '2002-06-30'),
    (14, 'Cafu', 1, 2100, '2002-06-30'),
    (15, 'Kleberson', 2, 5700, '2002-06-30'),
    (16, 'Gilberto Silva', 1, 2100, '2002-06-30');

INSERT INTO cliente (idCliente, nome, endereco, telefone, email, ehFlamengo, ehOtaku, ehSousa)
VALUES
    (11, 'Sidney Magal', 'Rua dos Amores, 123', '11-987654321', 'sidney@example.com', false, false, false),
    (12, 'Odair José', 'Avenida das Paixões, 456', '11-999999999', 'odair@example.com', false, false, true),
    (13, 'Wando', 'Travessa dos Sonhos, 789', '11-111111111', 'wando@example.com', false, true, false),
    (14, 'Reginaldo Rossi', 'Praça do Amor, 789', '11-222222222', 'reginaldo@example.com', false, true, true),
    (15, 'Amado Batista', 'Rua da Saudade, 321', '11-333333333', 'amado@example.com', true, false, false),
    (16, 'Gabigol', 'Avenida do Golaço, 666', '21-987654321', 'gabigol@example.com', true, false, true),
    (17, 'Bruno Henrique', 'Rua dos Dribles, 777', '21-999999999', 'brunohenrique@example.com', true, true, false),
    (18, 'Everton Ribeiro', 'Travessa dos Passes, 888', '21-111111111', 'evertonribeiro@example.com', true, true, true),
    (19, 'Arrascaeta', 'Praça das Assistências, 999', '21-222222222', 'arrascaeta@example.com', true, true, true),
    (20, 'Diego Alves', 'Rua dos Defesas, 333', '21-333333333', 'diegoalves@example.com', true, true, true);