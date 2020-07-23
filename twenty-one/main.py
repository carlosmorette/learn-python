from functions import giveLetter
from colors import colors

colorBank = colors["Azul"]
colorPlayer = colors["Amarelo"]

print("{0}JOGO 21{0}".format(colors["Verde"]))

print("{0}={0}".format(colors["Azul"]) * 35)

firstCardBank = giveLetter()
print("{2}Primeira carta da banca: {0} de {1}{2}".format(
    firstCardBank["name"], firstCardBank["naipe"], colorBank))

print("{0}={0}".format(colors["Azul"]) * 35)

firstCardPlayer = giveLetter()
print("{2}Sua primeira carta: {0} de {1}{2}".format(
    firstCardPlayer["name"], firstCardPlayer["naipe"], colorPlayer))

print("{0}={0}".format(colors[3]["value"]) * 35)

secondCardBank = giveLetter()
print("{0}Segunda carta da banca: oculta{0}".format(colorBank))

print("{0}={0}".format(colors[3]["value"]) * 35)

secondCardPlayer = giveLetter()
print("{2}Sua segunda carta: {0} de {1}{2}".format(
    secondCardPlayer["name"], secondCardPlayer["naipe"], colorPlayer))

print("{0}={0}".format(colors[3]["value"]) * 35)

sumBank = firstCardBank["value"] + secondCardBank["value"]
sumPlayer = firstCardPlayer["value"] + secondCardPlayer["value"]

print("{1}A banca está com {0}{1}".format(firstCardBank["value"], colorBank))
print("{1}Vocẽ está com {0}{1}".format(sumPlayer, colorPlayer))

if sumBank != 21 and sumPlayer != 21:
    ifMoreCard = str(input("Deseja mais uma carta?[s/n]"))
elif sumBank == 21:
    print("A banca venceu!")
elif sumPlayer == 21:
    print("Você venceu!")
