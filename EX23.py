alunos = int(input("Digite a quantidade de alunos: "))
soma = 0
i = 1
while i <= alunos:
    numero = int(input("Digite a média do aluno: "))
    soma+=numero
    i=i+1
media= soma/alunos
print("A média dos aritmética é:", media)7