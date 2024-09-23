import os

print('Exemplo com While: \n')
num = -1

while num <= 0:
    os.system('cls')
    num = int(input('Digite um numero positivo : '))

print('voce digitou ', num)