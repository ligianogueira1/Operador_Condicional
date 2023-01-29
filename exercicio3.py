#Questão3

#Faça um programa que leia três números e mostre o maior deles.

print("======================")
print("Welcome to the program!")
print("======================")
value1 = float(input("To start, enter the first number: "))
value2 = float(input("To start, enter the second number: "))
value3 = float(input("To start, enter the third number: "))

bigger = value1

if value2 > bigger:
    bigger = value2

if value3 > bigger:
    bigger = value3

print(f"The bigger number entered is: {bigger}.")
