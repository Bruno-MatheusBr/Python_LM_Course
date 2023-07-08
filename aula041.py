# while / else

string = "Valor qualquer"

i = 0

while i < len(string):
    if string[i] == " ":
        print("Espaço encontrado.")
        break
    print(string[i])
    i += 1
else:
    print("Nenhum espaço encontrado!")
print("Saiu do while.")
