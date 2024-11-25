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
            componente.manutencao_preventiva()

    def manutencao_corretiva(self):
        for componente in self.componentes:
            componente.manutencao_corretiva()

    def __str__(self):
        # Exibe as informações de todos os componentes no formato desejado
        componentes_info = "\n".join([str(componente) for componente in self.componentes])
        return f"Computador {self.id}:\n{componentes_info}"
