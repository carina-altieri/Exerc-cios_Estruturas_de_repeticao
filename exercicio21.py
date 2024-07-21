# 21
# .Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
# As turmas não podem ter mais de 40 alunos. '''

turmas = int(input('Quantidade de turmas: '))

total_alunos = 0

for t in range(1, turmas + 1):
    
    while True:
        alunos_por_turma = int(input(f'Informe a quantidade de alunos na Turma {t}: '))
     
        if  alunos_por_turma <= 40:
            total_alunos += alunos_por_turma
            break
        else:
            print('Entrada inválida. As turmas não podem conter mais de 40 alunos.')

media = total_alunos / turmas
print(f'Média de alunos por turma: {media:.2f}')