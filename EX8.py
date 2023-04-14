time1 = input("Digite o primeiro time: ")
golt1 = int(input("Gols: "))
time2 = input("Digite o segundo time: ")
golt2 = int(input("Gols: "))
if golt1 != golt2:
    if golt1 > golt2:
        print("Vencedor:", time1)
    else:
        print("Vencedor:", time2)
else:
    print("Empate!")