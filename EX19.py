cont=0
for x in range(10):
    n = int(input("Digite um número: "))
    if n <0:
        cont+=1
print("O total de números negativos é de: ", cont)