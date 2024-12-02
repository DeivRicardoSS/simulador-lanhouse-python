import random

def ligarPc(pcs):
    for pc in pcs:
        if not pc.ligado:
            if random.randint(0, 10) == 9:
                pc.ligado = True
        else:
            if random.randint(0, 10) == 9:
                pc.ligado = False
            
        