# while True:
#     print("Vai demorar muitoooooo")

from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input("Informe o número: "))

print("Numero secreto {} foi encontrado!".format(numero_secreto))