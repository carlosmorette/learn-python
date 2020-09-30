import random

random_number = random.randint(1, 10)

number_kick = None
while number_kick != random_number:
    print(random_number)
    number_kick = int(input("Chute um numero de 1 a 10: "))

print(f"Você acertou: {random_number}")