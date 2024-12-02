import time
from utilities.clear import clear
from modules.pc import Pc
from calc.reportar import reportar

class Program:
    #Construtor
    def __init__(this):
        #dia
        this.dia = 0
        #minutos
        this.minutos = 0
        #horas
        this.horas = 8
        #temporeal
        this.timerate = 0.5
        #lista de manutenção
        this.lista_manutencao = []
        #lista de computadores
        this.pcs = [
            Pc("Maquina 1"),
            Pc("Maquina 2"),
            Pc("Maquina 3")
        ]

        while True:
            #limpar tela
            clear()
            #printar dia e horário
            print(f"Dia {this.dia:02} | {this.horas:02}h{this.minutos:02}")
            #ligando pcs de forma aleatória
            for pc in this.pcs: pc.ligarPc()
            #listando pcs
            this.listar_pcs()
            #definindo intervalo de tempo
            time.sleep(this.timerate)
            
            #sistema de protgreção de tempo
            this.minutos += 1
            if this.minutos == 60:
                this.minutos = 0
                this.horas += 1
            if this.horas == 19:
                this.horas = 8
                this.dia += 1
            #===============================
                
    

    def listar_pcs(this):
        #percorrer computadores
        for pc in this.pcs:
            #printar status
            print(f"\nNome: {pc.id.ljust(15)} | Ligado: {pc.ligado} | Status: {pc.status.ljust(15)}\nComponentes: ")
            #percorrer componentes
            for comp in pc.componentes:
                #printar status dos componentes
                print(f"Nome: {comp.id.ljust(15)} | Quebrado: {comp.quebrado} | Tempo de vida: {comp.tempo_de_vida:.2f} | Custo: {comp.custo}")
                if pc.ligado:
                    comp.quebrarRand()
                #caso o componente quebrou o pc desliga
                if comp.quebrado == True:
                    pc.ligado = False
                    if pc.tempo_de_inatividade < 10:
                        pc.status = "Quebrado"
                    else:
                        if comp.erro == 1:
                            reportar(comp, this.timerate, this.lista_manutencao, "corretiva")
                            pc.status = "Funcionando"
                    
                    pc.tempo_de_inatividade += 1
                        
                    
                else:
                    #Computador Não Está quebrado
                    #vida útil dos componentes diminui
                    if pc.ligado and comp.tempo_de_vida > 0: comp.vidautil()
                    elif comp.tempo_de_vida <= 0:
                        #se o tempo de vida chegar a 0 o pc desliga 
                        comp.quebrado = True
                        pc.ligado = False
                        pc.status = "Quebrado"
                        reportar(comp, this.timerate, this.lista_manutencao, "corretiva")
                        pc.status = "Funcionando"
                
            

Program()