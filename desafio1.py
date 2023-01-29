#Desafio1

#Faça um programa que leia, via linha de comando, três números, e mostre-os em ordem decrescente.

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])

list = [num1, num2, num3]

list.sort(reverse=True)

print(f"The numbers entered, in descending order, are: {list}.")
