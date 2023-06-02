CREATE OR REPLACE PROCEDURE AtualizarStatusVenda(idveiculo_id INT)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE veiculo
    SET statusvenda = true
    WHERE idveiculo = idveiculo_id;
END;
$$;
