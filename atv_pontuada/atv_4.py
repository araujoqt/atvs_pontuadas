import os

os.system("clear")

print("""
======================  MENU ======================   
Código     \tAté 5KG         \tAcima de 5KG
1 Morango  \tR$2,50 por KG   \tR$2,20 por KG
2 Maçã     \tR$1,80 por KG   \tR$1,50 por KG

""")

quantidade_de_macas = int(input("Digite a quantidade de maçãs: "))
quantidade_de_morangos = int(input("Digite a quantidade de morangos: "))

macas = float(2.50)
maca_2 = float(2.20)
morango = float(1.80)
morango_2 = float(1.50)

if quantidade_de_macas or quantidade_de_morangos <=5:
    total = (quantidade_de_morangos * morango) + (quantidade_de_macas * macas)
    print(f"Total: {total}")
elif quantidade_de_macas or quantidade_de_morangos > 8:
    total = (quantidade_de_morangos * morango) + (quantidade_de_macas * macas)
    total_final = (total*0.10)
    print(f"Valor a pagar: {total_final}")