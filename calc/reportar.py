import time
from calc.calctime import calctime
from modules.manut import Manut
from calc.calccusto import calccusto

def reportar(item, timerate, lista_manutencao, tipo):
    
    lista_manutencao.append(Manut(len(lista_manutencao), calccusto(tipo, item.preco, 50), "corretiva", item)) 
    item.custo += calccusto(tipo, item.preco, 50)
    item.quebrado = False
    item.quant_preventiva = 0
    item.tempo_de_vida = 100

def trocar(item, lista_manutencao):
    if item.tipo == "original":
        lista_manutencao.append(Manut(len(lista_manutencao), calccusto("preventiva", item.preco, 50), "preventiva", item))
        item.tipo = "temporaria"
        item.tempo_de_vida = 100
    else:
        item.quant_preventiva += 1
        item.tipo = "original"
        item.tempo_de_vida = 80
        item.custo += calccusto("preventiva", item.preco, 50)
        
