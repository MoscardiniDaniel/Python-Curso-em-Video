"""
Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a media de cada um e permita que o usário possa mostrar as notas
de cada aluno individualmente
"""
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"nº.":<4}{"Nome":<10}{"Media":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
