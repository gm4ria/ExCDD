n1 = float(input("Digite o primeiro número:"))
n2 = float(input("Digite o segundo número:"))
if n1!=n2:
    if n1<n2:
        print("Ordem crescente.", n1, "e", n2)
    else:
        print("Ordem decrescente.", n2, "e", n1)
else:
    print("Números iguais, tente novamente com valores distintos!!")