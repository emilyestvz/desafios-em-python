valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do salário do comprador: R$'))
anos = int(input('Qts anos de financiamento? '))

prestacao = valor_casa / (anos * 12)
minimo = salario * 30 / 100

if prestacao <= minimo:
    print('Empréstimo pode ser concedido! A prestação será de R$ {prestacao:.2f}')
else: 
    print(f'Empréstimo NEGADO!')
