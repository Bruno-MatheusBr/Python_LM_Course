# contador = 0

# while contador <= 100:
#     contador += 1

#     if contador > 10 and contador < 30:
#         print('Não vou mostrar o ', contador)
#         continue
#     print(contador)

#     if contador == 40:
#         break

contador = 0

while contador < 100:
    contador += 1
    if contador > 10 and contador < 20:
        continue
    print(contador)

    if contador == 40:
        break

print("Acabou!!! 🙌")
