from modules.computador import Comp

class Pc:
    def __init__(this, id):
        this.id = id
        this.ligado = False
        this.status = "Funcionando"
        this.componentes = [ 
            Comp("cpu"), 
            Comp("memoria"), 
            Comp("placa_mae"), 
            Comp("memoria_ram"), 
            Comp("fonte")
        ]
                            