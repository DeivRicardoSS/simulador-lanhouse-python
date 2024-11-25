from modules.pc import Pc


class Program:
    def __init__(self, atualizar_interface_callback):
        self.computadores = [
            Pc("Máquina 1"),
            Pc("Máquina 2"),
            Pc("Máquina 3"),
        ]
        self.dinheiro = 1000
        self.atualizar_interface_callback = atualizar_interface_callback

    def manutencao_preventiva(self, pc):
        if self.dinheiro >= 50:
            pc.manutencao_preventiva()
            self.dinheiro -= 50
            self.atualizar_interface_callback()
        else:
            print("Dinheiro insuficiente para manutenção preventiva!")

    def manutencao_corretiva(self, pc):
        if self.dinheiro >= 30:
            pc.manutencao_corretiva()
            self.dinheiro -= 30
            self.atualizar_interface_callback()
        else:
            print("Dinheiro insuficiente para manutenção corretiva!")
