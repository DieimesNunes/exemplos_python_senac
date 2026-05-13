import os
os.system("cls")

nota = float(input('Escreva sua nota.....:  '))
if( nota >= 90):
    print('A - Excelente')
elif (nota >= 60):
    print ("B - Regular")
else:
    print ("Reprovado")