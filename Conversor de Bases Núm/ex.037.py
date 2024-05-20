num = int(input('Digite um número inteiro: '))
print('''Escolha uma base de conversão: 
      [1] converter para Binário
      [2] converter para Octal 
      [3] converter para Hexadecimal''')
opcao = int(input('Escolha uma opção: '))

b = bin(num).replace('0b', '')
o = oct(num).replace('0o', '')
h = hex(num).replace('0x', '').upper()

if opcao == 1:
    print(f'O número {num} convertido para Binário é igual a: {b}.')
elif opcao == 2:
    print(f'O número {num} convertido para Octal é igual a: {o}.')
elif opcao == 3:
    print(f'O número {num} convertido para Hexadecimal é igual a: {h}.')
else:
    print('Você não escolheu uma das opções.')
