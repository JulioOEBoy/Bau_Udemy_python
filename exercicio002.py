numero = input("Digite um número inteiro para saber se é par ou impar: ")
if int(numero) % 2 == 0:
    print(f"O número {numero} é par.")
if int(numero) % 2 != 0:
    print(f"O número {numero} é impar.")
else:
    print("Digite apenas números inteiros.")