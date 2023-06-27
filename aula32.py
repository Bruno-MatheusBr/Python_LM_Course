"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero_usuario = input('Digite um número inteiro: ')
# try:
#     numero_usuario_inteiro = int(numero_usuario)
#     if (numero_usuario_inteiro % 2) == 0:
#         print('O número digitado é par')
#     else:
#         print('O número digitado é impar')
# except:
#     print('O número digitado não é um número inteiro.')





"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# hora = input('Digite a hora em número inteiro: ')
# try:
#     hora_int = int(hora)
#     if hora_int >= 0 and hora_int < 12:
#         print('Bom dia!')
#     elif hora_int > 11 and hora_int < 18:
#         print('Boa tarde!')
#     elif hora_int >= 18 and hora_int < 24:
#         print('Boa noite!')
#     else:
#         print('Essa hora não existe.')
# except:
#     print('Por favor, digite apenas números inteiros.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

name = input('Escreva seu primeiro nome: ')
name_lenght = len(name)

if name_lenght > 1:
    if name_lenght <= 4:
        print('Seu nome é muito curto.')
    elif name_lenght <= 6:
        print('Seu nome é correto.')
    else:
        print('Seu nome é muito grande.')
else:
    print('Digite pelo menos duas letras.')