import random

class Computador:
    def __init__(this, id):
        this.id = id
        this.custo = 0
        this.tempo_de_vida = 100
        this.quebrado = False
        this.preco = 0
        
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
    
    # def quebrarRand():
    #     if random.randint(0, 10) == 9:
    #         return True
        
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