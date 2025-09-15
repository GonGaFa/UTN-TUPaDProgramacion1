resultado = 1

for num in range(1,6):
    resultado *= num
    if resultado > 10:
        break

print(resultado)