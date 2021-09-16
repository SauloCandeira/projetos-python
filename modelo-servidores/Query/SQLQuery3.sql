/****** Script do comando SelectTopNRows de SSMS  ******/
SELECT TOP (1000) 
       [cpf] CPF
      ,[nome] NOME
	  ,CONCAT(CONCAT(SUBSTRING ([cpf],5,3),SUBSTRING ([cpf],9,3)),REPLACE([nome],' ','')) CHAVE
  FROM [bdBI].[dbo].[uniao_servidores] 
  
  
  --ON  CONCAT(CONCAT(SUBSTRING ([cpf],5,3),SUBSTRING ([cpf],9,3)),REPLACE([nome],' ','')) = 
  --,REPLACE([nome],' ','') NOME_SEM_ESPACO