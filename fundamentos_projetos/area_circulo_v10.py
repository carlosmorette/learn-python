#!/usr/bin/python3
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == "__main__":
    raio = sys.argv[1]  # first argument value
    area = circulo(raio)
    print(area)
