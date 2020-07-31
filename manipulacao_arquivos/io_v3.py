arquivo = open("pessoas.csv")
for registro in arquivo:
    # the strip function removes white spaces from the edges of the string
    print("Nome: {} Idade: {}".format(*registro.strip().split(",")))
arquivo.close()
