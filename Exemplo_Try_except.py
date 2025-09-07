numero_str = input("Digite um número para eu dobrar: ")

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f"O dobro de {numero_float} é {numero_float * 2}")
except:
    print("Isso não é um número válido.")
    print("Por favor, digite apenas números.")

