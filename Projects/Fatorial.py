#Crie um programa que recebe um número e imprime o seu fatorial.
'''
1-Entrada: número
2-Calcular o fatorial e imprimí-lo
3-O número precisa ser inteiro e positivo
4- n! = n(n - 1)(n - 2)*...*1
                    n vezes
Algoritmo:
input fatorial = 1
input numero
loop de 1 a numero
    fatorial = fatorial *numero
print fatorial
'''
numero = int(input('Digite um número inteiro e positivo: '))
fatorial = 1
if numero > 0:
    for item in range(fatorial, numero + 1):
        fatorial = fatorial * item
print(fatorial)
