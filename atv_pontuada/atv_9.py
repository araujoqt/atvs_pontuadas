import os 

os.system("clear")

renda_mensal = float(input("Digite o valor da sua renda: "))
valor_emprestimo = float(input("Digite o valor do empréstimo:  "))
num_prestacoes = int(input("Digite o número de prestações desejadas: "))

valor_prestacao = valor_emprestimo / num_prestacoes

if valor_emprestimo <= 10 * renda_mensal and valor_prestacao <= 0.30 * renda_mensal:
    print("Empréstimo autorizado!")
else:
    print("Empréstimo não autorizado!")