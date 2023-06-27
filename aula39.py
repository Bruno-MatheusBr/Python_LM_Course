# Exercício de While

nome = 'Bruno Matheus'
tamanho = len(nome)
indice = 0
novo_nome = ''

while indice < tamanho:
    letra = nome[indice] + "*"
    novo_nome += letra  # novo_nome = novo_nome + letra
    indice += 1

print(novo_nome)
