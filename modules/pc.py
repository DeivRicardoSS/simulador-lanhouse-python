from modules.computador import Computador 

class Pc:
    def __init__(this, id):
        this.id = id
        this.ligado = False
        this.status = "Funcionando"
        this.componentes = [ 
            Computador("cpu"),
            Computador("memoria"),
            Computador("placa_mae"),
            Computador("memoria_ram"),
            Computador("fonte")
        ]
