nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
if nome and idade:
    print(f"Olá {nome}")
    print(f"Seu nome ao contrario é {nome[::-1]}")
    if nome.isalpha():
        print("Seu nome contém apenas letras")
    else:
        print("Seu nome contém números ou caracteres especiais")
        print(f"seu nome contem espaços? {' ' in nome}")
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")
