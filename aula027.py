"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade de caracteres da str
"""
variavel = "Olá Mundo"
print(variavel[4])  # Índice específico da esquerda pra direita
print(variavel[-4])  # Índice específico da direita pra esquerda
print(variavel[4:])  # Fatiamento definindo início mas não o fim
print(variavel[:3])  # Fatiamento definindo fim mas não o início
print(variavel[1:3])  # Fatiamento definindo início e fim
print(variavel[::2])  # Pula caracteres
print(variavel[::-1])  # Inverte a str
print("")
print(len("Bruno Matheus Soares Domingues"))
print(len(variavel[0:4]))
