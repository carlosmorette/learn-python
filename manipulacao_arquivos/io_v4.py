'''
finally is used when you want to execute a piece of
code regardless of whether or not there was an error
'''
try:
    arquivo = open("pessoas.csv")
    for registro in arquivo:
        print("Nome: {} Idade: {}".format(*registro.strip().split(",")))
finally:
    print('Finally')
    arquivo.close()
