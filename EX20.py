cont=0
cont2=0
for x in range(10):
    n = int(input("Digite um número: "))
    if n >= 10 and n <=20:
        cont+=1
    else:
        cont2=cont2+1
print(cont)
print(cont2)