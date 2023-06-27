'''
Introdução ao try/except
try -> tenta executar um código.
except -> ocorreu algum erro ao executar o código.
'''

# print(123)
# print(456)
# int('a') # Nesse ponto vai dar erro porque não é possível converter str em int.

# numero = input('Vou dobrar o número que vc digitar: ')
# numero_inteiro = int(numero)

# print(f'O dobro de {numero} é {numero_inteiro * 2}') #toda essa expressão resulta erro se digitado uma letra.

numero_str = input('Vou dobrar o número que vc digitar: ')

try:
    numero_real = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_real * 2:.2f}')

except:
    print('O valor digitado não é um número')

# float('a')
