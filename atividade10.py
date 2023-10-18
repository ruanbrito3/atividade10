# Exercício Python 10: faça um algoritimo que receba a velocidade em Km/h de um veiculo e:
# se maior que 60km/h aplicar multa de 7 vezes a da velocidade permitida
n1 = int(input("digite a velocidade"))
if (n1>60) :
    print ("multa")
multa = (n1-60)*7
print (f"sua multa é {multa}")