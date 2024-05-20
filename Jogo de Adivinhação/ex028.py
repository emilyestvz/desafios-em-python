print(f'-=-' * 20)
print(f'\t\tJOGO DA ADIVINHAÇÃO')
print(f'-=-' * 20)

from random import randint
from time import sleep
pc = randint(0, 10) # faz o pc "pensar"


print(f'Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print(f'-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print(f'ESPERA AI Q EU TO PENSANDO...')
sleep(2)

if jogador == pc:
    print(f'Aêeeee krl, parabéns, você acertou!')
else:
    print(f'Aaaah, você errou 😢\nEu pensei no número {pc} e não no {jogador}. Tenta de novo!!!')

