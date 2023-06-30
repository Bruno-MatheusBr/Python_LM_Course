"""
Introdução ao try/except
try -> tenta executar um código.
except -> ocorreu algum erro ao executar o código.
"""

# print(123)
# print(456)
# int('a') # Nesse ponto vai dar erro porque não é possível converter str em int.

# numero = input('Vou dobrar o número que vc digitar: ')
# numero_inteiro = int(numero)

# print(f'O dobro de {numero} é {numero_inteiro * 2}') #toda essa expressão resulta erro se digitado uma letra.

print("Vou dobrar o número que vc digitar!")
numero_str = input("Digite um número: ")

try:
    numero_real = float(numero_str)
    numero_dobrado = numero_real * 2
    print(f"O valor dobrado de {numero_real:.2f} é {numero_dobrado:.2f}.")

except:
    print("Você não digitou um número.")
    print("Por favor, digite um número.")
