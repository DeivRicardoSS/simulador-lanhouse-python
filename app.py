import tkinter as tk
from datetime import datetime
from main import Program

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulador de Lan House")

        # tamanho da janela inicial
        self.root.geometry("450x850")

        # Informações principais
        self.label_data_hora = tk.Label(self.root, text="", font=("Arial", 14))
        self.label_data_hora.pack(pady=10)

        # Botão iniciar
        self.button_iniciar = tk.Button(self.root, text="Iniciar", font=("Arial", 14), command=self.iniciar)
        self.button_iniciar.pack(pady=20)

        # Inicializando o programa, mas ainda sem exibir os computadores
        self.program = Program(self.atualizar_interface)

        # Lista para armazenar os nomes dos componentes dos computadores
        self.computadores_labels = []

        # atualizando nome da função para nome de usuario
        self.mapeamento_componentes = {
            "cpu": "Processador",
            "memoria": "Memória",
            "placa_mae": "Placa Mãe",
            "memoria_ram": "Memória RAM",
            "fonte": "Fonte"
        }

        # Inicializa a interface
        self.root.mainloop()

    def iniciar(self):
        """Função chamada quando o botão 'Iniciar' é pressionado"""
        # Remove o botão iniciar da tela
        self.button_iniciar.pack_forget()

        # Criação dos computadores
        self.criar_computadores()

        # Atualiza a interface a cada segundo
        self.atualizar_interface()

    def criar_computadores(self):
        """Criação dos computadores e seus componentes"""
        # Nomes para os computadores
        nomes_computadores = ["Computador 1", "Computador 2", "Computador 3"]

        # Exibe o dinheiro na tela de computadores
        self.label_dinheiro = tk.Label(self.root, text=f"Dinheiro: R$ {self.program.dinheiro:.2f}", font=("Arial", 14))
        self.label_dinheiro.pack(pady=10)

        self.frame_computadores = tk.Frame(self.root)
        self.frame_computadores.pack()

        for idx, pc in enumerate(self.program.computadores):
            frame = tk.Frame(self.frame_computadores, borderwidth=2, relief="groove", padx=10, pady=10)
            frame.pack(pady=5)

            # Título do computador
            tk.Label(frame, text=nomes_computadores[idx], font=("Arial", 12, "bold")).pack()

            # Adiciona os nomes dos componentes
            for componente in pc.componentes:
                nome_amigavel = self.mapeamento_componentes.get(componente.id, componente.id)  # Usa o nome amigável
                label = tk.Label(frame, text=f"{nome_amigavel}: {componente}", font=("Arial", 10))
                label.pack()
                self.computadores_labels.append(label)

            # Botões de manutenção
            tk.Button(frame, text="Preventiva (R$ 50)", command=lambda p=pc: self.program.manutencao_preventiva(p)).pack(pady=5)
            tk.Button(frame, text="Corretiva (R$ 30)", command=lambda p=pc: self.program.manutencao_corretiva(p)).pack(pady=5)

    def atualizar_interface(self):
        """Atualiza as informações na interface sem recriar os widgets"""
        # Atualiza a data e hora
        self.label_data_hora.config(text=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

        # Atualiza o valor do dinheiro
        self.label_dinheiro.config(text=f"Dinheiro: R$ {self.program.dinheiro:.2f}")

        # Atualiza os componentes dos computadores
        label_idx = 0
        for pc in self.program.computadores:
            for j, componente in enumerate(pc.componentes):
                nome_amigavel = self.mapeamento_componentes.get(componente.id, componente.id)  # Usa o nome amigável
                self.computadores_labels[label_idx].config(text=f"{nome_amigavel}: {componente}")
                label_idx += 1  # Incrementa o índice para o próximo componente

        # Chama a função de atualização da interface a cada 1000ms (1 segundo)
        self.root.after(1000, self.atualizar_interface)


if __name__ == "__main__":
    App()
