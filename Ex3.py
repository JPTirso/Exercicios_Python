listaProduto = []
listaCli = []
vendasRealizadas = 0
totalVendas = 0
while True:
    try:
        while True:
            i = 0
            nome = input("Digite o nome do produto: ")
            nomesIguais = False
            while i<len(listaProduto):
                if nome.lower() == listaProduto[i]["nome"]:
                    nomesIguais = True
                i+=1
            if nomesIguais == False:
                break
            else:
                print("Não podemos ter produtos com nomes iguais, digite outro nome de produto: ")
            

        Produto = {
            "nome": nome,
            "preco": float(input("Digite o preço do produto: ")),
            "estoque": int(input("Digite a quantidade em estoque: "))
        }
        listaProduto.append(Produto)
        continuar = input("Digite 'N' se você não deseja continuar cadastrando produtos, digite qualquer outra tecla se deseja continuar: ")
        if continuar.lower() == "n":
            break
    except ValueError:
        print("Você digitou um valor errado no cadastro de produtos")
while True:
    nomeCli = input("Digite seu nome: ")
    total = 0
    while True:
        nomeProduto = input("Digite o nome do produto que deseja comprar")
        produtoEncontrado = False
        i = 0
        while i<len(listaProduto):
            if listaProduto[i]["nome"].lower() == nomeProduto.lower():
                produtoEncontrado = True
                while True:
                    try:
                        qtd = int(input("Digite a quantidade de " + nomeProduto + " que desja comprar: "))
                        if (listaProduto[i]["estoque"] - qtd) >= 0:
                            listaProduto[i]["estoque"] -= qtd
                            subtotal = listaProduto[i]["preco"]*qtd
                            total += subtotal
                            break
                        else: 
                            print("Não temos estoque o suficiente para esse produto, digita outra quantidade")
                    except:
                        print("Quantidade invalida digite novamente")
            i += 1
        if produtoEncontrado == False:
            print("O produto digitado não foi encontrado")
        if total>0:
            continuar = input("Digite 'N' se você não deseja continuar comprando produtos, digite qualquer outra tecla se deseja continuar: ")
            if continuar.lower() == "n":
                break
    if total >= 1000:
        desconto = 0.15
    elif total >= 500:
        desconto = 0.10
    elif total >= 200:
        desconto = 0.05
    else:
        desconto = 0
    Cliente = {
        "nomecli": nomeCli,
        "totalVenda": total - (total*desconto)
        }
    listaCli.append(Cliente)
    continuar = input("Digite 'N' deseja parar de comprar, digite qualquer outra tecla se deseja continuar como outro cliente: ")
    if continuar.lower() == "n":
        break
maiorVenda = listaCli[0]["totalVenda"]
cliMaiorVenda = listaCli[0]["nomecli"]
i = 0
while i<len(listaCli):
    totalVendas += listaCli[i]["totalVenda"]
    if maiorVenda<listaCli[i]["totalVenda"]:
        maiorVenda = listaCli[i]["totalVenda"]
        cliMaiorVenda = listaCli[i]["nomecli"]
    i+=1
media = totalVendas/len(listaCli)

print(vendasRealizadas)
print(totalVendas)
print(cliMaiorVenda)
print(media)
                
        

