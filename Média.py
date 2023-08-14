Materia1 = float( input("Nota da primeira Materia: ") )
Materia2 = float( input("Nota da segunda Materia: ") )
Materia3 = float( input("Nota da terceira Materia: ") )

media = (Materia1 + Materia2 + Materia3) / 3

print("A média desse estudante foi: ",media)
if media >= 70.00:
    print('O aluno foi Aprovado com a média ', media, )

else:
    print('O aluno foi Reprovado com a média ', media, )
