from cartas import cartas
import random

# Give random card


def giveLetter():
    chosenLetter = random.choice(cartas)
    cartas.remove(chosenLetter)
    return chosenLetter
