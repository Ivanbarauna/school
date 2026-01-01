# Crie um código que pede 2 número para o usuário;
# Os 2 números são somados, multiplicados, com uma condição
# Se os número forem pares ele faz a multiplicação, se forem impars ele só faz a soma.

# AND, IF, ELSE, SOMA, MULTIPLICACAO

number1 = int(input("Digite o número 1:"))
number2 = int(input("Digite o nùmero 1:"))

# if number1 % 2 == 0 and number2 % 2 == 0:
#     resultado = number1 * number2
#     print(f"Ambos são pares, e o resultado da multiplicação é: {resultado}")
# else: 
#     resultado = number1 + number2
#     print(f"Há números impares. O Resultado soma um total de: {resultado}, ")

print(f"Resultado: {number1 * number2 if number1 % 2 == 0 and number2 % 2 == 0 else number1 + number2}")


