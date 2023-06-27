entrada = input('Digite E para Entrar ou S para Sair: ')
senha = input('Senha: ')
print(entrada)

if entrada == 'E':
    print(senha)
    if senha == '1234':
        print('Você entrou.')
    else:
        print('Senha incorreta.')

else entrada == 'S':
    print('Você saiu')
# else:
   # print('Por favor, digite E ou S')

