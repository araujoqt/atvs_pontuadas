import os 

os.system("clear")

print("""
==================== POSTO DE COMBUSTIVEL====================   
A = Álcool 3.79R$
G = Gasolina 6.59R$

""")

comb = input("Digite o tipo de combustível: ").upper()
litros = float(input("Digite a quantidade de litros: "))

if comb == "A":
    preco = 3.79
    tipo = "Álcool"

elif comb == "G":
    preco = 6.59
    tipo = "Gasolina"

match comb:
    case "A":
        if litros <= 25:
            desconto = preco *0.02
        else:
            desconto = preco *0.04
    case "G":
        if litros <= 25:
            desconto = preco * 0.03
        else:
            desconto = preco * 0.05
    
    case _:
        print("Combustível não encontrado")
        exit()

    valor = preco * litros
    valorfinal = valor - desconto