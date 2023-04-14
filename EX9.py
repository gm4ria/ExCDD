comb1 = input("Qual combustível vendido?")
litros = float(input("Quantos litros vendidos?"))
if comb1 in " G":
    valor_total = litros * 5.8
    print(valor_total)
elif comb1 in  " E":
    valor_total = litros * 4.9
    print(valor_total)
else:
    print("Tipo inválido!")