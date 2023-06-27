a = "A"
b = "B"
c = 1.1
# string = 'a={} b={} c={:.2f} d={}'
# formato = string.format(a, b, c, a)

# string = 'a={0} b={1} c={2}' # todas as str tem que utilizaro o método de número
# formato = string.format(a, b, c)

# string = 'a={nome1} b={nome2} c={nome3}'
# formato = string.format(nome1=a, nome2=b, nome3=c)

string = "a={} b={} c={:.2f}".format(a, b, c)
# formato = string.format(a, b, c)
print(string)

# // Teste Pessoal
nome = "Bruno"
sobrenome = "Domingues"

nome_completo = "{} {}".format(nome, sobrenome)
print(nome_completo)

# // PARÂMETRO NOMEADO
print("")  # Espaçamento
print("Formato Nomeado")  # Título

string_2 = "b= {nome2} a= {nome1} c= {nome3:.2f}"
formato_nomeado = string_2.format(nome1=a, nome2=b, nome3=c)
print(formato_nomeado)
