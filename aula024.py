nome = input("Digite seu nome: ")
encontrar = input("Qual letra vc quer verificar? ")

if encontrar in nome:
    print(f'"{encontrar}" está em {nome}.')
else:
    print(f'"{encontrar}" não está em {nome}.')
