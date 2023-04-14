nomealuno = input("Qual o seu nome?")
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
media = nota1 + nota2 + nota3
mediafinal = media / 3
print(f"A media de {nomealuno} é {mediafinal}")

if mediafinal>= 7:
    print("Aluno aprovado!")

elif mediafinal>= 4:
    print("Aluno em reciuperação!")

else:
    print("Aluno reprovado!")