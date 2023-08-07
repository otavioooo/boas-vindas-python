import math

angulos = float(input("Digite um número: "))
seno = math.sin(math.radians(angulos))
cosseno = math.cos(math.radians(angulos))
tangente = math.tan(math.radians(angulos))
print(f'O seno do ângulo {angulos} é {seno:.2f}')
print(f'O cosseno do ângulo {angulos} é {cosseno:.2f}')
print(f'A tangente do ângulo {angulos} é {tangente:.2f}')