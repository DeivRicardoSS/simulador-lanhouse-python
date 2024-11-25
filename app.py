import tkinter as tk
from datetime import datetime
from main import Program

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulador de Lan House")

        # Informações principais
        self.label_data_hora = tk.Label(self.root, text="", font=("Arial", 14))
        self.label_data_hora.pack()

        self.label_dinheiro = tk.Label(self.root, text="Dinheiro: R$ 1000", font=("Arial", 14))
        self.label_dinheiro.pack()

        # Área dos computadores
        self.frame_computadores = tk.Frame(self.root)
        self.frame_computadores.pack()

        self.program = Program(self.atualizar_interface)

        # Inicializando lista para armazenar labels dos componentes
        self.computadores_labels = []

        # Criação inicial dos computadores para garantir que todos sejam exibidos
        self.criar_computadores()

        # Atualiza a interface inicialmente
        self.atualizar_interface()

        self.root.mainloop()

    def criar_computadores(self):
        """Criação dos computadores e seus componentes"""
        for idx, pc in enumerate(self.program.computadores):
            frame = tk.Frame(self.frame_computadores, borderwidth=2, relief="groove", padx=10, pady=10)
            frame.pack(pady=5)

            # Título do computador
            tk.Label(frame, text=f"Computador {idx + 1}", font=("Arial", 12, "bold")).pack()

            # Adiciona os labels dos componentes
            for componente in pc.componentes:
                label = tk.Label(frame, text=str(componente), font=("Arial", 10))
                label.pack()
                self.computadores_labels.append(label)

            # Botões de manutenção
            tk.Button(frame, text="Preventiva (R$ 50)", command=lambda p=pc: self.program.manutencao_preventiva(p)).pack(pady=5)
            tk.Button(frame, text="Corretiva (R$ 30)", command=lambda p=pc: self.program.manutencao_corretiva(p)).pack(pady=5)

    def atualizar_interface(self):
        """Atualiza as informações na interface sem recriar os widgets"""
        # Atualiza a data e hora
        self.label_data_hora.config(text=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

        # Atualiza o dinheiro
        self.label_dinheiro.config(text=f"Dinheiro: R$ {self.program.dinheiro:.2f}")

        # Atualiza os componentes dos computadores
        label_idx = 0
        for pc in self.program.computadores:
            for j, componente in enumerate(pc.componentes):
                self.computadores_labels[label_idx].config(text=str(componente))
                label_idx += 1  # Incrementa o índice para o próximo componente

        # Chama a função de atualização da interface a cada 1000ms (1 segundo)
        self.root.after(1000, self.atualizar_interface)


if __name__ == "__main__":
    App()
