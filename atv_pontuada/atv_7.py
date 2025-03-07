import os 

os.system("clear")

nome_produto = input("Digite o nome do produto: ")
quant = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: "))

total = quant * preco_unitario

if quant <= 5:
    desconto = total * 0.10  
elif 5 < quant <= 10:
    desconto = total * 0.03  
else:
    desconto = total * 0.05 

total_a_pagar = total - desconto

print()
print(f"Nome do produto: {nome_produto}")
print(f"Total: R${total}")
print(f"Desconto: R${desconto}")
print(f"Total a pagar: R${total_a_pagar}")
