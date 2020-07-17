from cartas import cartas
import math
import random

# Give random card
def giveLetter():
  cartaEscolhida = random.choice(cartas)
  cartas.remove(cartaEscolhida)
  return cartaEscolhida
