import os 

os.system("clear")

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

if a == b:
    soma = a + b
    c = (soma)
    print(f"O valor de C é {c}")
else:
    multiplicacao = (a * b)
    c = multiplicacao
    print(f"O valor de C é {c}")