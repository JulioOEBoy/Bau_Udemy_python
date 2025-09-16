contador = 0

while contador < 2:
    contador += 1
    nome = str(input('Me diga o seu nome: '))
    idade = int(input("digite a sua idade: "))
    peso = float(input("Digite aqui o seu peso: "))
    cpf = int(input("digite o seu cpf: "))
    print(f'Seu nome é {nome}, sua idade é {idade}, seu peso é {peso} e seu cpf é {cpf}')
    if idade >= 18:
        print('Você é maior de idade')
    else:
        print('Você é menor de idade')
    if peso >= 50:
        print('Você está acima do peso')
    else:
        print('Você está dentro do peso')
    if cpf >= 11:
        print('Seu cpf é válido')
    else:
        print('Seu cpf é inválido') 
    if nome == 'sair':
        break
    if idade == 0:
        break
    if peso == 0:
        break
    if cpf == 0:
        break
    if contador == 2:
        break
    print(f'Você já cadastrou {contador} pessoas')
print('Você atingiu o limite de cadastros')
