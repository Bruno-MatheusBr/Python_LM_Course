"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força os caracteres extras a aparecer no lado esquerdo.
Sinal - + ou -
Ex.: 0>-100,1.f
Conversion flags - !r !s !a
"""
variavel = "ABC"

print(f".{variavel:>8}.")
print(f".{variavel:0>8}.")  # Utilizado em contas numéricas
print(f".{variavel:<8}.")
print(f".{variavel:0<8}.")
print(f".{variavel:0^8}.")
print("")
print("Restringindo casas decimais e colocando vírgula para separar milhar")
print(f"{1000.848539457834}")
print(f"{1000.848539457834:.2f}")
print(f"{1000.848539457834:,.2f}")
print("")
print("Mostrando se o número é positivo (+) ou negativo (-)")
print("Para mostrar os dois sinais, usa-se somente o sinal de + na F-String")
print(f"{1000.848539457834:+,.2f}")  # Importante
print(f"{-1000.848539457834:+,.2f}")  # Importante
print("")
print(
    "Caso extremo: forçar o sistema a colocar zeros antes do número e o sinal de mais ou menos"
)
print('Usa-se o sinal de "=" no lugar de ">"')
print(f"{-1000.848539457834:0=+10,.2f}")
print("")
print("Hexadecimal com F-String")
print(f"O Hexadeciaml de 1500 é {1500:x}")
print(f"O Hexadeciaml de 1500 é {1500:05x}")  # Força o Hexadecimal ter 5 dígitos
numero = 2000

print(f"O exadecimal de {numero} é {numero:05X}")
