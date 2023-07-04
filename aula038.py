# while dentro de while

# qtd_linhas = 5
# qtd_colunas = 5

# linha = 1

# while linha <= qtd_linhas:
#     coluna = 1

#     while coluna <= qtd_colunas:
#         print(f'{linha=} {coluna=}')
#         coluna += 1

#     linha += 1

# print('Acabou!')

nr_linhas = 5
nr_colunas = 5

linha = 0
coluna = 0

while linha < nr_linhas:
    linha += 1
    while coluna < nr_colunas:
        coluna += 1
        print(f"Linha {linha} - Coluna {coluna}")
    coluna = 0

print("Acabou 🙌🙌🙌")
