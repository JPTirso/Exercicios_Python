# Exercício Prático Integrador — Sistema de Cadastro Vendas (Console) 
# Crie um programa em Python que funcione como um sistema simples de cadastro e 
# vendas, seguindo os requisitos abaixo: 
# Passo 1 -  Cadastro de produtos 
# O programa deve: 
# ➢ perguntar quantos produtos serão cadastrados  
# ➢ para cada produto, solicitar:  
# ✓ nome do produto  
# ✓ preço  
# ✓ quantidade em estoque  
# ➢ armazenar os produtos em uma lista  
# ➢ cada produto deve ser representado por um dicionário  
# Passo 2 -  Realização da venda 
# Depois do cadastro, o programa deve: 
# ➢ solicitar o nome do cliente  
# ➢ permitir a compra de vários produtos  
# ➢ perguntar o nome do produto desejado  
# ➢ verificar se o produto existe  
# ➢ solicitar a quantidade desejada  
# ➢ calcular o subtotal da compra de cada item  
# ➢ somar tudo no total geral da compra
# Passo 3 -  Regras de desconto 
# Ao final da compra, aplicar as seguintes regras: 
# ➢ se o total for maior ou igual a 1000 → desconto de 15%    
# ➢ se o total for maior ou igual a 500 e menor que 1000 → desconto de 10%  
# ➢ se o total for maior ou igual a 200 e menor que 500 → desconto de 5%  
# ➢ caso contrário → sem desconto  
# Passo 4 -  Repetição da compra 
# O programa deve perguntar se o cliente deseja continuar comprando produtos. 
# Enquanto a resposta for diferente de N, o sistema deve continuar permitindo novas 
# compras. 
# Passo 5 -  Exibição final 
# Ao final, mostrar: 
# ➢ nome do cliente  
# ➢ produtos comprados  
# ➢ total da compra  
# ➢ valor do desconto  
# ➢ total final 

listaProdutos = []
produtosComprados = ""
qntCadastrada = int(input("insira quanto produtos serão cadastrados: "))
i = 0
total = 0
while i < qntCadastrada:
    Produto = {
        "nome": input("Insira o nome do produto: ").lower(),
        "preco": float(input("Insira o preço do produto: ")),
        "qntEstoque": int(input("Insira a quanrtidade desse produto em estoque: ")),
        "id": i
    }
    i+=1
    listaProdutos.append(Produto)
nomeCli = input("Insira seu nome: ")
while True:
    qntCompra = int(input("Insira quantos produtos deseja comprar: "))
    j = 0
    while j < qntCompra:
        nomeProdutoCli = input("Insira o nome do produto desejado: ")
        i = 0
        produtoExiste = False
        while i < len(listaProdutos):
            if listaProdutos[i]["nome"] == nomeProdutoCli.lower():
                produtoExiste = True
                qtdCli = int(input("Insira a quantidade desejada: "))
                subtotal = qtdCli * listaProdutos[i]["preco"]
                total += subtotal
                produtosComprados += nomeProdutoCli + ", "
                break
            i += 1       
        if produtoExiste == False:
            print("Esse produto não existe")
            j -= 1
        j += 1
    resposta = input("Insira 'n' caso você não deseja continuar comprando. Caso contrario digite qualquer coisa: ")
    if resposta == "n":
        break

if total >= 1000:
    desconto = 0.15
elif total >= 500:
    desconto = 0.1
elif total >= 200:
    desconto = 0.05
else:
    desconto = 0
print (nomeCli)
print (produtosComprados)
print (total)
print ("Não teve desconto" if desconto == 0 else "Seu desconto foi de " + desconto + "%")
print ((total/(desconto+1)))






    
    

