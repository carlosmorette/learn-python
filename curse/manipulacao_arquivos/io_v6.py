with open('pessoas.csv') as arquivo:
    with open("pessoas.txt", "w") as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            # using the file resource it is determined
            # that the output of the function will be in the given file
            print("Nome: {} Idade: {}".format(*pessoa), file=saida)

if arquivo.closed:
    print("Arquivo já foi fechado!")

if saida.closed:
    print("Arquivo de saída já foi fechado!")
