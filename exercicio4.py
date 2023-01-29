#Questão4

#Faça um programa que leia via input de usuário um número correspondente a um determinado ano e, em seguida, informe se este ano é ou não bissexto.

print("======================")
print("Welcome to the leap year checker!")
print("======================")
year = int(input("To start, enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is leap.")
else:
    print("The year not is leap.")
