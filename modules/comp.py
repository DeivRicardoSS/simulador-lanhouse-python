import random
from calc.reportar import reportar

class Comp:
    #construtor
    def __init__(this, id):
        #id
        this.id = id
        #custo
        this.custo = 0
        #tempo de vida
        this.tempo_de_vida = 100
        #não está quebrado
        this.quebrado = False
        #preço
        this.preco = 0

        this.erro = 0
        
        #separando os preços de acordo com a peça
        if this.id == "cpu":
            this.preco = 500
        elif this.id == "memoria":
            this.preco = 400
        elif this.id == "placa_mae":
            this.preco = 400
        elif this.id == "memoria_ram":
            this.preco = 200
        elif this.id == "fonte":
            this.preco = 150
        #=========================================
        
    #cacular decremento de cida útil de acordo com a peça
    def vidautil(this):
        if this.id == "cpu":
            this.tempo_de_vida -= 0.2
        elif this.id == "memoria":
            this.tempo_de_vida -= 0.3
        elif this.id == "placa_mae":
            this.tempo_de_vida -= 0.5
        elif this.id == "memoria_ram":
            this.tempo_de_vida -= 0.4
        elif this.id == "fonte":
            this.tempo_de_vida -= 0.8
    #======================================================

    #quebrar aleatoriamente
    def quebrarRand(this):
        if random.randint(0, 1000) < 10 and not this.quebrado:
            this.quebrado = True
            this.erro = 1
            return True
        return False