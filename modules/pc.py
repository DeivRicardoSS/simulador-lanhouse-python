from modules.computador import Computador


class Pc:
    def __init__(self, id):
        self.id = id
        self.componentes = [
            Computador("cpu"),
            Computador("memoria"),
            Computador("placa_mae"),
            Computador("memoria_ram"),
            Computador("fonte")
        ]

    def manutencao_preventiva(self):
        for componente in self.componentes:
            componente.tempo_de_vida = 100
            componente.quebrado = False

    def manutencao_corretiva(self):
        for componente in self.componentes:
            if componente.quebrado:
                componente.tempo_de_vida = 80
                componente.quebrado = False
