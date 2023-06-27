condicao = True

while condicao:
    nome = input('Escreva seu nome: ')
    if nome != 'sair':
        print(f' Seu nome é {nome}.')
    else:
        break

print('Acabou')
