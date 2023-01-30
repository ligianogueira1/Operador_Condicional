#Desafio2

#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime:
#1) "Falou com a vítima no dia do crime?"
#2) "Esteve no local do crime?"
#3) "Mora perto da vítima?"
#4) "Devia dinheiro para a vítima?"
#5) "Já trabalhou com a vítima?"

#Se a pessoa responder positivamente a 2 questões, ela deve ser classificada como "Suspeita"; entre 3 e 4, como "Cúmplice"; e 5, como "Assassina". Caso contrário, ela será classificada como "Inocente".

print("======================")
print("Investigação do crime")
print("======================")

perguntas = [
    "Falou com a vítima no dia do crime? \n",
    "Esteve no local do crime? \n",
    "Mora perto da vítima? \n",
    "Devia dinheiro para a vítima? \n",
    "Já trabalhou com a vítima? \n"
]

respostas = 0

for p in perguntas:
    r = input(p)
    if r == "Sim" or r == "sim":
        respostas += 1
    elif r == "Não" or r == "não":
        continue
    else:
        r = input(p)
        while(r != "Sim" or r != "sim" or r != "Não" or r!= "não"):
            r = input(p)
            if r == "Sim" or r == "sim":
                respostas += 1
                break
            elif r == "Não" or r == "não":
                break

if respostas == 5:
    print("Esta pessoa é a assassina do crime!")
elif respostas == 3 or respostas == 4:
    print("Esta pessoa é cúmplice do assassinato!")
elif respostas == 2:
    print("Esta pessoa é suspeita do crime!")
else:
    print("Esta pessoa é inocente!")
