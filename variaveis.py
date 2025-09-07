velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro se encontra

radar_1 = 60 # velocidade máxima do radar 1
local_1 = 100 # local onde o radar 1 está posicionado
radar_ranger = 1 # o radar pega 1 km antes e 1 km depois do local do radar

velocidade_carro_passou_radar = velocidade > radar_1
carro_passou_radar_1 = local_carro >= (local_1 - radar_ranger) and \
        local_carro <= (local_1 + radar_ranger)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar

if velocidade > radar_1:
    print("Você passou pelo radar 1.")

if carro_passou_radar_1:
    print("O carro passou pelo radar 1.")

if carro_passou_radar_1 and velocidade > radar_1:
    print("Você foi multado por excesso de velocidade no radar 1.")
