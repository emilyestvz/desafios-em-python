import time
from datetime import date
atual = date.today().year

nasc = int(input('Ano de nascimento: '))
idade = atual - nasc

print(f'O atleta tem {idade} anos...')
time.sleep(2)

if idade >= 25:
    print(f'Sua classificação: MASTER')
elif idade <= 25:
    print(f'Sua classificação: SÊNIOR')
elif idade <= 19:
    print(f'Sua classificação: JUNIOR')
elif idade <= 14:
    print(f'Sua classificação: INFANTIL')
elif idade <= 9:
    print(f'Sua classificação: MIRIM')
else: 
    print(f'Não entendi o que foi digitado. Tente novamente.')
