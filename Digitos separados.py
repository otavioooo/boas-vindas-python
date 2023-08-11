numero = int(input('Digite um número de 0 a 9999: '))

milhar = numero // 1000

centena = (numero% 1000) // 100

dezena = ((numero % 1000) % 100) // 10

unidade = ((numero % 1000) % 100) // 10

print(f'Unidade: {unidade}')

print(f'Centena: {centena}')

print(f'Milhar: {milhar}') 