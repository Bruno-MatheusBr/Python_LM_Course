frase = "O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum."

i = 0
quantidade = 0
letra = ""

while i < len(frase):
    letra_atual = frase[i]
    quantidade_atual = frase.count(letra_atual)
