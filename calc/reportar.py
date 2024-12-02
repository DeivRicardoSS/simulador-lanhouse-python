import time
from calc.calctime import calctime
from modules.manut import Manut
from calc.calccusto import calccusto

def reportar(item, timerate, lista_manutencao, tipo):
    
    lista_manutencao.append(Manut(len(lista_manutencao), calccusto(tipo, item.preco, 50), "corretiva", item)) 
    item.custo += calccusto(tipo, item.preco, 50)
    item.quebrado = False
    item.tempo_de_vida = 100