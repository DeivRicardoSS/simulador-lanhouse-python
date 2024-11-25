import tkinter as tk
from tkinter import ttk
from datetime import datetime
from main import Program

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulador de Lan House")

        # Tamanho inicial da tela e configuração de redimensionamento
        self.root.geometry("1366x768")  # Tamanho inicial
        self.root.minsize(800, 600)  # Tamanho mínimo para não reduzir demais
        self.root.config(bg="#2c3e50")

        # Título da janela
        self.title_label = tk.Label(self.root, text="Simulador de Lan House", font=("Arial", 24, "bold"), bg="#2c3e50", fg="white")
        self.title_label.pack(pady=20)

        # Informações principais (data e hora)
        self.label_data_hora = tk.Label(self.root, text="", font=("Arial", 16), bg="#2c3e50", fg="white")
        self.label_data_hora.pack(pady=10)

        # Dinheiro (para mostrar o valor disponível)
        self.label_dinheiro = tk.Label(self.root, text="Dinheiro: R$ 1000.00", font=("Arial", 18), bg="#2c3e50", fg="white")
        self.label_dinheiro.pack(pady=10)

        # Botão iniciar
        self.button_iniciar = tk.Button(self.root, text="Iniciar", font=("Arial", 18), command=self.iniciar, bg="#16a085", fg="white", relief="flat", padx=20, pady=10)
        self.button_iniciar.pack(pady=20)

        # Inicializando o programa, mas ainda sem exibir os computadores
        self.program = Program(self.atualizar_interface)

        # Lista para armazenar os nomes dos componentes dos computadores
        self.computadores_labels = []

        # Mapeamento de componentes para exibir nomes amigáveis
        self.mapeamento_componentes = {
            "cpu": "Processador",
            "memoria": "Memória",
            "placa_mae": "Placa Mãe",
            "memoria_ram": "Memória RAM",
            "fonte": "Fonte"
        }

        # Frame de computadores que será redimensionável
        self.computadores_frame = tk.Frame(self.root, bg="#2c3e50")
        self.computadores_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Inicia a interface
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

        # Adiciona uma margem maior entre os computadores
        for idx, pc in enumerate(self.program.computadores):
            frame = tk.Frame(self.computadores_frame, borderwidth=2, relief="groove", bg="#ecf0f1", padx=15, pady=20, width=400)
            frame.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")  # Usando grid para controle de posição

            # Título do computador
            tk.Label(frame, text=nomes_computadores[idx], font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=5)

            # Adiciona os nomes dos componentes
            for componente in pc.componentes:
                nome_amigavel = self.mapeamento_componentes.get(componente.id, componente.id)  # Usa o nome amigável
                label = tk.Label(frame, text=f"{nome_amigavel}: {componente}", font=("Arial", 14), bg="#ecf0f1", anchor="w", wraplength=250)  # Adicionando wraplength
                label.pack(fill="x", pady=5)
                self.computadores_labels.append(label)

            # Botões de manutenção (estilizados)
            buttons_frame = tk.Frame(frame, bg="#ecf0f1")
            buttons_frame.pack(pady=15)

            tk.Button(buttons_frame, text="Preventiva (R$ 50)", command=lambda p=pc: self.program.manutencao_preventiva(p), font=("Arial", 14), bg="#27ae60", fg="white", relief="flat", padx=20, pady=5).pack(side="left", padx=10)
            tk.Button(buttons_frame, text="Corretiva (R$ 30)", command=lambda p=pc: self.program.manutencao_corretiva(p), font=("Arial", 14), bg="#e74c3c", fg="white", relief="flat", padx=20, pady=5).pack(side="left")

        # Configuração de expansão para as colunas
        for col in range(3):  # Como temos 3 computadores
            self.computadores_frame.grid_columnconfigure(col, weight=1, uniform="computador")

        # Configuração de expansão para a linha de computadores (no caso, temos uma linha de computadores)
        self.computadores_frame.grid_rowconfigure(0, weight=1)

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
