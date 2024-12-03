   #Como o custo vai ser caulculado       
def calccusto(tipo, preco, maodeobra):
    if tipo == "preventiva":
        return preco/3 + maodeobra
    else:
        #custo da corretiva é o preço + 0.3 x (inatividade_em_minutos / 1 hora)
        return preco + 0.3 * (10/60)
    