numerador = int(input("Digite um número: "))
print("\n")
for i in range(1,11):
    r = numerador/i
    print("{} / {} = {}".format(numerador,i,r))
    i = i/i
