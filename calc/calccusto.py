   #Como o custo vai ser caulculado       
def calccusto(tipo, preco, maodeobra):
    if tipo == "preventiva":
        return preco/3 + maodeobra
    else:
        return preco + 0.3 * 10