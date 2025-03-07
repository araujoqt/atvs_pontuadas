import os 

os.system("clear")

n1 = int(input('Número um: '))
n2 = int(input('Número dois: '))

print()
media = (n1 + n2) / 2
soma = (n1 + n2) 
multi = (n1 * n2) 

if media <= 4 or media >= 6:
    print("Parabéns!")
else:
    print("Recuperação!")

print(f"Media: {media}")