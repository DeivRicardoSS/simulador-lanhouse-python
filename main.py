import time
from utilities.clear import clear
from modules.pc import Pc
from calc.ligarpc import ligarPc
# from calc.reportar import reportar  # Descomente se for necessário

class Program:
    def __init__(this):
        this.dia = 0
        this.minutos = 0
        this.horas = 0
        this.timerate = 0.5
        this.lista_manutencao = []
        # Lista de computadores
        this.pcs = [
            Pc("Maquina 1"),
            Pc("Maquina 2"),
            Pc("Maquina 3")
        ]

        while True:
            clear()
            # Printar dia, data e hora no terminal
            print(f"Dia {this.dia:02} | {this.horas:02}h{this.minutos:02}")
            ligarPc(this.pcs)
            this.listar_pcs()
            time.sleep(this.timerate)
            this.minutos += 1
            if this.minutos == 60:
                this.minutos = 0
                this.horas += 1
            if this.horas == 8:
                this.horas = 0
                this.dia += 1

    def listar_pcs(this):
        for pc in this.pcs:
            print(f"\nNome: {pc.id} | Ligado: {pc.ligado}\nComponentes: ")
            for computador in pc.componentes:
                print(f"Nome: {computador.id} | Quebrado: {computador.quebrado} | Tempo de vida: {computador.tempo_de_vida:.2f} | Custo: {computador.custo}")
                if computador.quebrado:
                    pc.ligado = False
                else:
                    # Computador Não Está quebrado
                    if pc.ligado and computador.tempo_de_vida > 0:
                        computador.vidautil()
                    if computador.tempo_de_vida <= 0:
                        pc.status = "Quebrado"
                    elif computador.tempo_de_vida <= 0:
                        computador.quebrado = True
                        pc.ligado = False

program = Program()
