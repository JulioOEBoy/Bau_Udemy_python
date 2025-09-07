hora = input("Digite a hora atual: ")

try:
    hora = int(hora)

    if int(hora) < 0 or int(hora) > 11:
        print("Bom dia!")
    if int(hora) >= 12 and int(hora) < 17:
        print("Boa tarde!")
    if int(hora) >= 18 and int(hora) <= 23:
        print("Boa noite!")
except:
    print("Por favor, digite um número inteiro entre 0 e 23.")
        