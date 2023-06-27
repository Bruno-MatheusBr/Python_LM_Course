nome = "Bruno Matheus"
altura = 1.82
peso = 80
imc = peso / altura**2

# f-strings: formata strings
linha_1 = f"{nome} tem {altura}m de altura."
linha_2 = f"Pesa: {peso}kg"
linha_3 = f"Seu IMC é: {imc:.2f}"

print(linha_1)
print(linha_2)
print(linha_3)
