import random

class Computador:
    COMPONENTES_CONFIG = {
        "Cpu": {"preco": 500, "reducao_vida": 0.2},
        "Armazenamento": {"preco": 400, "reducao_vida": 0.3},
        "Placa mãe": {"preco": 400, "reducao_vida": 0.5},
        "Memória ram": {"preco": 200, "reducao_vida": 0.4},
        "Fonte": {"preco": 150, "reducao_vida": 0.8}
    }

    def __init__(self, id):
        if id not in Computador.COMPONENTES_CONFIG:
            raise ValueError(f"Componente '{id}' não reconhecido.")
        self.id = id
        self.tempo_de_vida = 100
        self.quebrado = False
        self.preco = Computador.COMPONENTES_CONFIG[id]["preco"]
        self.reducao_vida = Computador.COMPONENTES_CONFIG[id]["reducao_vida"]

    def vidautil(self):
        """Reduz a durabilidade do componente"""
        self.tempo_de_vida -= self.reducao_vida
        if self.tempo_de_vida <= 0:
            self.tempo_de_vida = 0  # Não permitir durabilidade negativa
            self.quebrado = True

    def quebrar_aleatorio(self):
        """Quebra o componente aleatoriamente com 10% de chance"""
        if random.randint(0, 9) == 9:
            self.quebrado = True

    def manutencao_preventiva(self):
        """Restaura a durabilidade para 100% e marca o componente como não quebrado"""
        self.tempo_de_vida = 100
        self.quebrado = False

    def manutencao_corretiva(self):
        """Corrige falhas e reduz um pouco a durabilidade"""
        if self.quebrado:
            self.tempo_de_vida = 80  # Um valor fixo após manutenção corretiva
            self.quebrado = False

    def __str__(self):
        """Retorna a descrição do componente"""
        return (f"{self.id.capitalize()}: Durabilidade {self.tempo_de_vida:.1f}% - "
                f"Quebrado: {'Sim' if self.quebrado else 'Não'}")
