from modules.computador import Computador

class Pc:
    def __init__(self, id):
        self.id = id
        self.ligado = False
        self.componentes = [
            Computador("CPU"),
            Computador("Memória"),
            Computador("Placa Mãe"),
            Computador("Memória RAM"),
            Computador("Fonte")
        ]

    def manutencao_preventiva(self):
        """
        manutenção preventiva, restaurando a durabilidade de todos os componentes para 100.
        """
        for componente in self.componentes:
            componente.tempo_de_vida = 100
            componente.quebrado = False
        print(f"Manutenção preventiva realizada no {self.id}. Durabilidade de todos os componentes restaurada para 100%.")

    def manutencao_corretiva(self):
        """
        manutenção corretiva, restaurando a durabilidade dos componentes quebrados para 80.
        """
        for componente in self.componentes:
            if componente.quebrado:
                componente.tempo_de_vida = 80
                componente.quebrado = False
        print(f"Manutenção corretiva realizada no {self.id}. Durabilidade dos componentes quebrados restaurada para 80%.")