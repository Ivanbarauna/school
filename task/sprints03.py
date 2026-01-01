# crie um programa que
# peça o valor de um produto
# peça a porcentagem de desconto
# mostre o valor final com o desconto
# o 2f ignora os número finais 


produto = float(input("Digite o valor da produto: "))
desconto = float(input("Digite o valor da desconto: "))

desconto = (produto * desconto) / 100

final = produto - desconto

# print(f"o desconto sera de: R$ {desconto:.2f}")
# print(f"o valor final com o desconto e: R$ {final:.2f}")

salario = float(input("Digite o valor do salario"))
aumento = salario * 0.15
novo = salario + aumento
print(f"o aumento sera de: R$ {aumento:.2f}")
print(f"o salario fianl de 15% e: R$ {novo:.2f}")