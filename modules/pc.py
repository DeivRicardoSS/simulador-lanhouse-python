import random  


from modules.comp import Comp

class Pc:
    #construtor
    def __init__(this, id):
        #id
        this.id = id
        #está desligado
        this.ligado = False
        #status
        this.status = "Funcionando"
        #tempo de inatividade
        this.tempo_de_inatividade = 0
        #lista de componentes
        this.componentes = [ 
            Comp("cpu"), 
            Comp("memoria"), 
            Comp("placa_mae"), 
            Comp("memoria_ram"), 
            Comp("fonte")
        ]
    #desligar ou ligar computador de forma randomica
    def ligarPc(this):
        #se tiver ligado
        if this.ligado:
            #desliga de forma aleatória
            if random.randint(0, 10) == 9:
                this.ligado = False
        elif this.ligado == False and this.status != "Quebrado":#se tiver desligado
            #liga de forma aleatória
            if random.randint(0, 10) == 9:
                this.ligado = True
                this.tempo_de_inatividade = 0
            