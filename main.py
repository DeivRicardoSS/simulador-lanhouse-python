from modules.computador import Computador
from modules.pc import Pc


class Program:
    def __init__(self, callback_atualizar):
        self.callback_atualizar = callback_atualizar
        self.computadores = [Pc(id=f"pc_{i}") for i in range(1, 4)]  # Inicializa os PCs

    def manutencao_preventiva(self, pc):
        """Simula manutenção preventiva para o PC"""
        pc.manutencao_preventiva()
        self.callback_atualizar()

    def manutencao_corretiva(self, pc):
        """Simula manutenção corretiva para o PC"""
        pc.manutencao_corretiva()
        self.callback_atualizar()

    def atualizar_interface(self):
        """Atualiza a interface com as informações dos componentes"""
        self.callback_atualizar()
