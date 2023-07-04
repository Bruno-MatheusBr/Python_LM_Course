condicao = True

while condicao:
    nome = input("Escreva seu nome: ")
    if nome != "sair" and nome != "Sair":
        print(f" Seu nome é {nome}.")
    else:
        break

print("Acabou")
