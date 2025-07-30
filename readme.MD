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

## Librarys 

- Para windows 
	- instalar pywin32 
	