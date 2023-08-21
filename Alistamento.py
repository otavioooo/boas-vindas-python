
from datetime import date

cores = {'del': '\033[m',
         'vermelho': '\033[1;31m'}

ano_nasc = int(input('Escreva o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nasc, idade, ano_atual))

if idade < 18:
    print('Ainda faltam {}{} ano(s){} para o alistamento\n'
          'Seu alistamento será em {}'.format(cores['vermelho'], 18 - idade, cores['del'], ano_atual + 18 - idade))
elif idade == 18:
    print('{}Já é hora de se alistar!{}'.format(cores['vermelho'], cores['del']))
elif idade > 18:
    print('Já passou/passaram {}{} ano(s){} da hora do alistamento!\n'
          'Seu alistamento era no {}'.format(cores['vermelho'], idade - 18, cores['del'], ano_atual - (idade - 18)))