from datetime import date
atual = date.today().year

nascimento = int(input('Seu ano de nascimento: '))
idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')

if idade == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print(f'Você ainda não tem 18 anos. Ainda faltam {18 - idade} anos para o alistamento...')
elif idade > 18:
    print(f'Você já deveria ter se alistado há {idade - 18} anos.')
