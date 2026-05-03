# Enunciado 
# Crie um programa em Python que simule um sistema simples de vendas, seguindo os 
# requisitos: 
# 1. Solicitar o nome do cliente  
# 2. Perguntar quantos produtos serão comprados  
# 3. Para cada produto:  
# ✓ solicitar nome do produto  
# ✓ solicitar preço  
# ✓ solicitar quantidade  
# ✓ calcular subtotal  
# 4. Somar o total da compra  
# 5. Aplicar regras:  
# ✓ se total ≥ 500 → desconto 10%  
# ✓ se total ≥ 200 e < 500 → desconto 5%  
# ✓ caso contrário → sem desconto  
# 6. Mostrar:  
# ✓ nome do cliente  
# ✓ total da compra  
# ✓ desconto  
# ✓ total final  
# 7. Perguntar se deseja realizar nova venda  
# # 8. Repetir até o usuário digitar "N" 
while True:
    nomeCli = input("Insira seu nome: ")
    qnt = int(input("insira quantos pordutos deseja comprar: "))
    i=0
    if qnt > 0:
        while i < qnt:
            nomeProduto = input("insira o nome do produto: ")
            preco = float(input("insira o preço de " + nomeProduto))
            qntProduto = int(input("insira a quantidade de " + nomeProduto ))
            subtotal = qntProduto*preco
            i += 1
            total = 0
            total += subtotal
        if total >= 500:
            desconto = 0.1
        elif total >= 200:
            desconto = 0.05
        else:
            desconto = 0
        print (nomeCli)
        print (total)
        print ("Não teve desconto" if desconto == 0 else "Seu desconto foi de " + desconto + "%")
        print ((total*(desconto+1)))

        resposta = input("deseja começar uma nova compra?(se não digite 'n')")
        if resposta.lower() == "n":
            break
    else:
        print("Valor invalido, reiniciando programa \n")