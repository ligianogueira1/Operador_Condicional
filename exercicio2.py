 #Questão 2

 #Faça um programa que peça uma idade via input de usuário e exiba uma mensagem informando se essa pessoa é maior ou menor de idade.

print("======================")
print("Welcome to the checker of age of majority!")
print("======================")
value = int(input("To start, enter your age: "))

if value >= 18:
    print("You are of legal age.")
else:
    print("You are underage.")
