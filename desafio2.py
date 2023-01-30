#Desafio2

#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime:
#1) "Falou com a vítima no dia do crime?"
#2) "Esteve no local do crime?"
#3) "Mora perto da vítima?"
#4) "Devia dinheiro para a vítima?"
#5) "Já trabalhou com a vítima?"

#Se a pessoa responder positivamente a 2 questões, ela deve ser classificada como "Suspeita"; entre 3 e 4, como "Cúmplice"; e 5, como "Assassina". Caso contrário, ela será classificada como "Inocente".

print("======================")
print("Crime investigation")
print("======================")

questions = [
    "Did you talk to the victim on the day of the crime? \n",
    "Were you been at the crime scene? \n",
    "Do you live near the victim? \n",
    "Did you owe the victim money? \n",
    "Have you ever worked with the victim? \n"
]

answers = 0

for q in questions:
    a = input(q)
    if a == "Yes" or a == "yes":
        answers += 1
    elif a == "No" or a == "no":
        continue
    else:
        a = input(q)
        while(a != "Yes" or a != "yes" or a != "No" or a!= "no"):
            a = input(q)
            if a == "Yes" or a == "yes":
                answers += 1
                break
            elif a == "No" or a == "no":
                break

if answers == 5:
    print("This person is the crime killer!")
elif answers == 3 or answers == 4:
    print("This person is an accomplice to the murder!")
elif answers == 2:
    print("This person is suspected of the crime!")
else:
    print("This person is innocent!")
