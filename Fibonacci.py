num1 = 0
num2 = 1
i = 2
qtd = int(input("Escreva até que numero de fibonath voce deseja mostrar: "))
if qtd > 0:
    print(num1)
    if qtd>1:
        print(num2)
    if qtd>2:
        while i<qtd:
            numNovo = num1 + num2
            print(numNovo)
            num2 = num1
            num1 = numNovo
            i+=1
else:
    print("Digite um numero valido")