#Questão5

#Faça um programa que leia via input de usuário os valores de duas notas de uma aluna. O programa deve calcular a média alcançada e apresentar:
#a) A mensagem "Aprovada", se a média alcançada for maior ou igual a 7;
#b) A mensagem "Reprovada", se a média alcançada for menor que 7;
#c) A mensagem "Aprovada com distinção", se a média alcançada for igual a 10.

print("======================")
print("Welcome to the approval checker!")
print("======================")
note1 = float(input("To start, enter the first note: "))
note2 = float(input("To start, enter the second note: "))

media = (note1 + note2)/2

if media == 10:
    print("Wow, you passed with distinction. Congratulations!")
elif media >= 7:
    print("Congratulations, the student was approved!")
else:
    print("Oops, the student failed!")
