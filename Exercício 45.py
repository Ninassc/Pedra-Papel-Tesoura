
import random
def linha():
    print('------------------------------------------------------')

linha()
print('Pedra, Papel, Tesoura')
linha()

vezes = int(input('Quantas vezes quer Jogar? '))
for vezes in range(vezes):
    numero = int(input('''Digite: 
    [0] Pedra
    [1] Papel
    [2] Tesoura: '''))

    jogadas = ['Pedra', 'Papel', 'Tesoura']
    aleatorio = random.choice(jogadas)

    if numero == 0 and aleatorio == 'Pedra':
         print('O computador também jogou PEDRA')
         print('Resultado: EMPATE')
    elif numero == 0 and aleatorio == 'Papel':
        print('O computador jogou PAPEL')
        print('Resultado: DERROTA')
    elif numero == 0 and aleatorio == 'Tesoura':
        print('O computador jogou TESOURA')
        print('Resultado: VITÓRIA')

    if numero == 1 and aleatorio == 'Pedra':
        print('O computador jogou PEDRA')
        print('Resultado: VITÓRIA')
    elif numero == 1 and aleatorio == 'Papel':
        print('O computador também jogou PAPEL')
        print('Resultado: EMPATE')
    elif numero == 1 and aleatorio == 'Tesoura':
        print('O computador jogou TESOURA')
        print('Resultado: DERROTA')

    if numero == 2 and aleatorio == 'Pedra':
        print('O computador jogou PEDRA')
        print('Resultado: DERROTA')
    elif numero == 2 and aleatorio == 'Papel':
        print('O computador jogou PAPEL')
        print('Resultado: VITÓRIA')
    elif numero == 2 and aleatorio == 'Tesoura':
        print('O computador também jogou TESOURA')
        print('Resultado: EMPATE')
    print(' ')
