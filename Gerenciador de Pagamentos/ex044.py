import time 
while True: 

    print(f'\n{" SEVILLANA'S ":💋^40}')
    preco = float(input('Valor total das suas compras: R$ '))
    print('''\tFORMAS DE PAGAMENTO
          [1] á vista dinheiro/cheque
          [2] á vista cartão de débito ou crédito
          [3] em 2x no cartão de crédito
          [4] em 3x ou mais no cartão de crédito
          ''')
    opcao = int(input('Qual é a opção? '))
    time.sleep(2)


    if opcao == 1:
        total = preco - (preco * 10/100)
        print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} com 10% de desconto. ✨')
    elif opcao == 2:
        total = preco - (preco * 5/100)
        print(f'Sua compra de R${preco:.2f} vai custar R${total:.2f} com 5% de desconto. ✨')
    elif opcao == 3:
        total = preco
        parcela = total / 2
        print(f'Sua compra de R${preco:.2f} e a parcela será R${parcela:.2f} em 2x no cartão de crédito. ✨')
    elif opcao == 4:
        total = preco + (preco * 20 / 100)
        totparc = int(input('Quantas parcelar? '))
        parcela = total / totparc
        print(f'Sua parcela de {totparc}x de R$ {parcela:.2f} (lembrando que esse é o valor do acréscimo de 20% de juros). ✨')
    else: 
        total = preco
        print(f'Opção inválida. Tente novamente. ✨')
        print(f'No total sua compra ficará {total:.2f}. Obrigada pela preferência 💖')

