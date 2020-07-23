produto = {"nome": "Caneta Chic", "preco": 14.99,
           "importada": True, "estoque": 793}

for chave in produto:  # traveled keys
    print(chave)

for valor in produto.values():
    print(valor)

for chaves, valor in produto.items():
    print(chaves, '=', valor)