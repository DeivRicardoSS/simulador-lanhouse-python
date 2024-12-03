   #Como o custo vai ser caulculado       
def calccusto(tipo, preco, maodeobra):
    if tipo == "preventiva":
        return preco/3 + maodeobra
    else:
        #nada a ver meu 3x o valor da peça
        #faria mais sentido se fosse só o valor da peça
        #mas você 🫵 que colocou no pdf que era pra ser assim
        return preco + 0.3 * 10
    