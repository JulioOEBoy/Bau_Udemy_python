hora = input("Digite a hora atual: ")
if int(hora) < 0 or int(hora) > 11:
    print("Bom dia!")
if int(hora) >= 12 and int(hora) < 17:
    print("Boa tarde!")
if int(hora) >= 18 and int(hora) <= 23:
    print("Boa noite!")
    