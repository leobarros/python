nomes = ["Leonardo", 31,
         ["Sabrina",31,
            ["Mariana",1]]]

def lista(li):
    for item in li:
        if isinstance(item, list):
            lista(item)
        else:
            print(item)


lista(nomes)

print(lista)
