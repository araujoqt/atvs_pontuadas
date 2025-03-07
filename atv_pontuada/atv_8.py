import os

os.system("clear")

print("Cores: Vermelho, Azul, Verde ou Amarelo")
c_cd = input("Digite a cor do CD: ").lower()

if c_cd == "vermelho":
    preco = 20.00
elif c_cd == "azul":
    preco = 30.00
elif c_cd == "verde":
    preco = 40.00
elif c_cd == "amarelo":
    preco = 50.00
else:
    print("Cor inválida")

print(f"O preço do CD {c_cd} é: R${preco:.2f}")
