condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faca algo")
else:
    print("Näo faca outra coisa")

if passou_no_if is None:
    print("Não passou no if")

if passou_no_if is not None:
    print("Não passou no if")