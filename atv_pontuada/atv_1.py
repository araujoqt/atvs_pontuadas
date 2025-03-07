import os

os.system("clear")

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

print()
soma = (a + b) 

print(f"Soma: {soma}")

if a + b > c:
    print("A e B é maior que C")
else:
    print("A e B é menor que C")