"""
r - Leitura
w - Escrita (sobrescrever)
a - Anexar ao final do arquivo
r+ = Leitura e escrita (adiciona)
"""

#Leitura de arquivo - Jeito errado
arquivo = open("Ex_Arquivos/Arquivos/teste.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()


#Jeito certo 
with open("Ex_Arquivos/Arquivos/teste.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#Sobrescrever um arquivo ou criar um novo arquivo
with open("Ex_Arquivos/Arquivos/teste2.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Ola Mundo rs")

#Anexar ao final
with open("Ex_Arquivos/Arquivos/teste2.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(" Ola Mundo 2")

#Ler e escrever adicionando no final
with open("Ex_Arquivos/Arquivos/teste2.txt", "r+", encoding="utf-8") as arquivo:
    #Move o cursor pro final
    antigo = arquivo.read()
    print(antigo)
    #Move o cursor pro inicio
    arquivo.seek(0)
    #Apaga tudo a frente do cursor
    arquivo.truncate()
    arquivo.write("Ola mundo dnv")
    arquivo.seek(0)
    novo = arquivo.read()
    print(novo)