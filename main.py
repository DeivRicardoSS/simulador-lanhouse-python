import time
from utilities.clear import clear
from modules.pc import Pc
from calc.ligarpc import ligarPc
#from calc.reportar import reportar

class Program:
    def __init__(this):
        this.dia = 0
        this.minutos = 0
        this.horas = 0
        this.timerate = 0.5
        this.lista_manutencao = []
        #lista de computadores
        this.pcs = [
            Pc("Maquina 1"),
            Pc("Maquina 2"),
            Pc("Maquina 3")
        ]

        while True:
            clear()
            #printar dia, data e hora no terminal
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
            for comp in pc.componentes:
                print(f"Nome: {comp.id} | Quebrado: {comp.quebrado} | Tempo de vida: {comp.tempo_de_vida:.2f} | Custo: {comp.custo}")
                if comp.quebrado:
                    pc.ligado = False
                else:
                    #Computador Não Está quebrado
                    if pc.ligado and comp.tempo_de_vida > 0: comp.vidautil()
                    if comp.tempo_de_vida <= 0: 
                        pc.status = "Quebrado"
                    elif comp.tempo_de_vida <= 0:
                        comp.quebrado = True
                        pc.ligado = False
                
            

program = Program()