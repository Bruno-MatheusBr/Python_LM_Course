# maior = 2 > 1
# maior_ou_igual = 2 >= 2
# menor = 2 < 2
# igual = 2 == 2
# diferente = 'a'  != 'b'

primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

if primeiro_valor > segundo_valor:
    print(
        f"O primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}"
    )
elif primeiro_valor == segundo_valor:
    print("Os valores são iguais")
else:
    print(
        f"O segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor}"
    )
