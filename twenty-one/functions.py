from cartas import cartas
import math
import random

# Dar uma carta aleatoria
def giveLetter():
  cartaEscolhida = random.choice(cartas)
  cartas.remove(cartaEscolhida)
  return cartaEscolhida