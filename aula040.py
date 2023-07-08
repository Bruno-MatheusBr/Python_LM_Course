# # Calculadora com While

# while True:
#     numero_1 = input('Digite um número: ')
#     numero_2 = input('Digite outro número: ')
#     operador = input('Digite um operador: ')

#     numero_valido = None
#     num_1_float = 0
#     num_2_float = 0

#     try:
#         num_1_float = float(numero_1)
#         num_2_float = float(numero_2)
#         numero_valido = True
#     except:
#         if numero_valido is None:
#             print('Um ou ambos os números são inválidos')
#             continue

#     operador_permitido = '+-*/'

#     if len(operador) > 1:
#         print('Digite somente um operador.')
#         continue
#     if operador not in operador_permitido:
#         print('Operador não permitido.')
#         continue

#     print ('O resultado é:')

#     if operador == "+":
#         print(num_1_float + num_2_float)

#     elif operador == '-':
#         print(num_1_float - num_2_float)

#     elif operador == '/':
#         print(num_1_float / num_2_float)

#     elif operador == '*':
#         print(num_1_float * num_2_float)


#     sair = input('Quer sair? [s]im: ').lower().startswith('s')

#     if sair is True:
#         break
#     else:
#         continue


calcular = True

while calcular:
    numero1 = input("Digite um número: ")
    numero2 = input("Digite outro número: ")
    operador = input("Digite o operador: ")

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)

        if operador == "+":
            print(
                f"{numero1_float} + {numero2_float} = {numero1_float + numero2_float}"
            )
        elif operador == "-":
            print(
                f"{numero1_float} - {numero2_float} = {numero1_float - numero2_float}"
            )
        elif operador == "*":
            print(
                f"{numero1_float} * {numero2_float} = {numero1_float * numero2_float}"
            )
        else:
            print(
                f"{numero1_float} / {numero2_float} = {numero1_float / numero2_float}"
            )

        sair = input('Deseja sair? Digite "s" para Sair ou "n" para continuar: ')
        sair = sair.lower()
        if sair == "s":
            break
        else:
            continue
    except:
        print("Você não digitou um número válido. Por favor tente novamente")
    continue

print("Você saiu!")
