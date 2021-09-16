--  DADOS I
--select nome, cpf, cargo from dbo.uniao_servidores

-- DADOS II 
--select NOM_PESSOA, NUM_CPF_PESSOA from tmp.TB_AUXILIO_GAS_20210810


-- MODELAGEM  --
select P.cpf,nome,cargo, PV.NUM_CPF_PESSOA, NOM_PESSOA from dbo.uniao_servidores P inner join tmp.TB_AUXILIO_GAS_20210810 PV
on CONCAT(CONCAT(SUBSTRING (P.[cpf],5,3),SUBSTRING (P.[cpf],9,3)),REPLACE(P.[nome],' ','')) = SUBSTRING(RIGHT('00000000000' + CAST(PV.[NUM_CPF_PESSOA] AS VARCHAR(11)),11),4,6) + REPLACE(PV.[NOM_PESSOA],' ','') 





