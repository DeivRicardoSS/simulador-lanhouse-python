import time
from calc.calctime import calctime
from main import program
from modules.manutencao import Manut
def reportar(itens):
    preco = 0
    for item in itens:
        preco += item.preco
    
    time.sleep(calctime(program.timerate, 1.30))
    program.lista_manutencao.append(Manut(range(program.lista_manutencao), preco, "corretiva", itens)
    )    