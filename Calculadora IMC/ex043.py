peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

print(f'Seu IMC seria de {imc:.2f} <3')

if imc < 18.5:
    print(f'Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print(f'Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'Você está com sobrepeso.')
elif 30 <= imc < 40:
    print(f'Você está com obesidade.')
else: 
    print(f'Você está com obesidade mórbida.')

