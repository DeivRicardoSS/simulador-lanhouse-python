import random

class Computador:
    # COMPONENTES
    COMPONENTES_CONFIG = {
        "cpu": {"preco": 500, "reducao_vida": 0.2},
        "memoria": {"preco": 400, "reducao_vida": 0.3},
        "placa_mae": {"preco": 400, "reducao_vida": 0.5},
        "memoria_ram": {"preco": 200, "reducao_vida": 0.4},
        "fonte": {"preco": 150, "reducao_vida": 0.8}
    }

    def __init__(self, id):
        if id not in Computador.COMPONENTES_CONFIG:
            raise ValueError(f"Componente '{id}' não reconhecido.")
        # ENCONTRAR COMPONENTES
        self.id = id
        self.custo = 0
        self.tempo_de_vida = 100
        self.quebrado = False

        # preço e redução de vida com base na configuração
        self.preco = Computador.COMPONENTES_CONFIG[id]["preco"]
        self.reducao_vida = Computador.COMPONENTES_CONFIG[id]["reducao_vida"]

    def vidautil(self):
        """
        Reduz o tempo de vida do componente.
        Se o tempo de vida chegar a zero, o componente será definido como quebrado.
        """
        self.tempo_de_vida -= self.reducao_vida
        if self.tempo_de_vida <= 0:
            self.quebrado = True # QUEBRA O COMPONENTE AO CHEGAR A 0

    def quebrar_aleatorio(self):
        """
        Define se o componente quebra com base em uma chance aleatória (10% de chance).
        """
        if random.randint(0, 9) == 9:  # 10% de chance de quebrar aleatoriamente
            self.quebrado = True

    def __str__(self): # RETORNO DAS INFORMAÇÕES !!
        return (f"Componente: {self.id}, Preço: {self.preco}, "
                f"Durabilidade: {self.tempo_de_vida:.1f}, Quebrado: {self.quebrado}")
