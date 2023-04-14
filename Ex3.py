nome = input("Nome:")
idade = float(input("Sua idade:"))
salario = float(input("R$:"))
percentual1 =  float (input ("Qual percentual de aumento?:"))

novo_salario = salario + salario * percentual1 / 100
print("\nnome:", nome, "\nidade:", idade, "\nR$:", salario)
print ("\nnovosalario:", novo_salario)