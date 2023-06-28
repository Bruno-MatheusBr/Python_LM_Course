entrada = input("Digite E para Entrar ou S para Sair: ")


if entrada == "E" or "e":
    senha = input("Senha: ")
    if senha == "1234":
        print("Você entrou.")
    else:
        print("Senha incorreta.")

elif entrada == "S" or "s":
    print("Você saiu")
else:
    print("Por favor, digite E ou S")
