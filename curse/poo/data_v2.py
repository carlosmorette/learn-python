class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"


d1 = Data(12, 12, 2012)
# d1.dia = 5
# d1.mes = 12
# d1.ano = 2000
print(d1)

d2 = Data(3, 6, 2000)
d2.dia = 7
d2.mes = 11
d2.ano = 2010
print(d2)
