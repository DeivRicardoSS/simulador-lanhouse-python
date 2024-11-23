import time
from utilities.clear import clear
from modules.pc import Pc
from calc.ligarpc import ligarPc

class Program:
    def __init__(self, callback):
        self.dia = 0
        self.minutos = 0
        self.horas = 0
        self.timerate = 0.5
        self.lista_manutencao = []
        self.pcs = [
            Pc("Maquina 1"),
            Pc("Maquina 2"),
            Pc("Maquina 3")
        ]
        self.callback = callback

    def iniciar(self):
        while True:
            clear()
            # Printar dia, data e hora no terminal
            print(f"Dia {self.dia:02} | {self.horas:02}h{self.minutos:02}")
            ligarPc(self.pcs)
            self.listar_pcs()
            self.callback(self.dia, self.horas, self.minutos, self.pcs)  # Atualizar a interface gráfica
            time.sleep(self.timerate)
            self.minutos += 1
            if self.minutos == 60:
                self.minutos = 0
                self.horas += 1
            if self.horas == 8:
                self.horas = 0
                self.dia += 1

    def listar_pcs(self):
        for pc in self.pcs:
            print(f"\nNome: {pc.id} | Ligado: {pc.ligado}\nComponentes: ")
            for computador in pc.componentes:
                print(f"Nome: {computador.id} | Quebrado: {computador.quebrado} | Tempo de vida: {computador.tempo_de_vida:.2f} | Custo: {computador.custo}")
                if computador.quebrado:
                    pc.ligado = False
                else:
                    if pc.ligado and computador.tempo_de_vida > 0:
                        computador.vidautil()
                    if computador.tempo_de_vida <= 0:
                        pc.status = "Quebrado"
                    elif computador.tempo_de_vida <= 0:
                        computador.quebrado = True
                        pc.ligado = False
