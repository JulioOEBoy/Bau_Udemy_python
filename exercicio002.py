numero = input("Digite um número inteiro para saber se é par ou impar: ")

if numero.isdigit():
    entrada = int(numero)
    if entrada % 2 == 0:
        print("O número é par.")
    if entrada % 2 != 0:
        print("O número é ímpar.")
else:
    print("Digite apenas números inteiros.")