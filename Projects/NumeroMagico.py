#Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.
#O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.
'''
1- Entrada: valor_aleatório, valor_usuário
2- O que fazer com as entradas?
Comparar o valor_aleatorio com valor_usuario e informar o resultado
3- Restrição: valor_usuario ser <1 ou >10
4- Algoritmo:
import random
input valor_usuario
input valor_aleatorio
if valor_usuario == valor_aleatorio
else valor_aleatorio != valor_usuario
print situacao
'''
import random
print('Desafio: Tente acertar o número mágico!')
valor_aleatorio = random.randint(1, 10)
acertou = False
while acertou == False:
    valor_usuario = int(input('Digite um número entre 1 e 10: '))
    if valor_usuario >= 1 and valor_usuario <= 10:
        if valor_usuario != valor_aleatorio:
            print('Você errou!')    
            if valor_usuario > valor_aleatorio:
                print('Seu número: ' + str(valor_usuario))
                print('Número mágico: ' + str(valor_aleatorio))
                print('Seu número está acima do número mágico!')
                print('Tente novamente! Obrigado por jogar!')
            else:
                print('Seu número: ' + str(valor_usuario))
                print('Número mágico: ' + str(valor_aleatorio))
                print('Seu número está abaixo do número mágico!')
                print('Tente novamente! Obrigado por jogar!')
        else:
            print('Parabéns! Você ganhou!')
            print('Seu número é igual ao número mágico!')
            print('Obrigado por jogar!')
            acertou == True
    else:
        print('Número inválido!')


