from modules.computador import Computador

class Pc:
    def __init__(this, id):

        this.id = id
        this.ligado = False
        this.status = "Funcionando"

        this.componentes = [
            Computador("cpu"),
            Computador("memoria"),
            Computador("placa_mae"),
            Computador("memoria_ram"),
            Computador("fonte")
        ]

class Componente:
    def __init__(self, id):
        self.id = id
        self.quebrado = False
        self.tempo_de_vida = 100
        self.custo = 50

    def vidautil(self):
        self.tempo_de_vida -= 0.5