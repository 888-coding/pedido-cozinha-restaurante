# Pedido para Cozinha de um restaurante 

## Impressão em impressora térmica

## Cadastro de produtos 

- Produtos:
	- ID do produto
		- int
	- Nome
		- text, 50
	- Valor
		- int 

- Pedidos:
	- ID do pedido
		- int, autoincremento
	- Numero da mesa 
		- text, 50 
	- Data do pedido
		-  Date
	- ID do produto
		- int
	- Nome do produto
		- text, 50
	- Valor do produto
		- int 

- Itens_Pedido* 
	- ID 
		- int, autoincremento
	- ID do Pedido 
		- int
	- ID do Produto 
		- int
	- quantidade
		- int
	- Preco unitario 
		- int

 * Isto é necessário porque é intermediario do pedido e produto 

## Pedidos feitos 

- Os produtos após ser feito tem que imprimir, 2 vias. 
	- Primeira via para o Caixa 
	- Segunda via para a Cozinha 

- Os pedidos devem ser gravados para futura consulta 
	- Consultar vendas 
	- Total do dia 
	- Total do mes 
	- Relatorio de mais vendidos 
	


# Problemas 

- Viagens: Precisa montar algo.

## Librarys 

- Para windows 
	- instalar pywin32 
	
## Problemas encontrados 

- Cadastro de pedido 
	- O valor total fica zerado as vezes. Provavelmente, é quando nao achou o codigo do produto. e portanto trava o sistema
		- Atualmente está cadastrando o pedido, e depois alterar o valor total do pedido, na tabela orders, com novo valor. Provavelmente, quando não encontramos os codigos do produto, acaba de não atualizar o valor, portanto, fica null. Causando erros futuros em Relatorios, e Vendas do dia.  Portanto, precisa verificar o codigo de produto existente antes de continuar, e também, repensar sobre o cadastro de pedido, na tabela orders, para mais tarde. 


- Relatório de vendas de todos os produtos 
	- A organização está errado, está puxando um valor do próximo código de produto . 

