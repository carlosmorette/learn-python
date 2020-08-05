generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))  # Output 0
print(next(generator))  # Output 4
print(next(generator))  # Output 16
print(next(generator))  # Output 36
print(next(generator))  # Output 64
# print(next(generator))  # Erro!
