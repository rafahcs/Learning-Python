#Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ele tomou um multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravíssima".

#Analise criticamente o problema e descubra:
#(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)
'''
Entrada: Velocidade
O que fazer com as entrada?
Guardar o valor, comparar com a velocidade permitida e retornar a situação do motorista
Restrição: velocidade = 0km/h o automóvel está parado
Resultados esperados: "Não hou mula", "Multa leve", "Multa grave","Multa gravíssima"
'''
velocidade_maxima = 80
velocidade = int(input('Qual é a velocidade do veículo: '))
if velocidade <= velocidade_maxima:
    print('Não levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('Levou multa leve')
elif velocidade > velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Levou multa grave')
else:
    print('Levou multa gravíssima')