import tkinter as tk
from datetime import datetime
from main import Program


class App:
    def __init__(self):
        print("Iniciando tkinter")  # Print para depuração

        self.root = tk.Tk()
        self.root.title("Simulador de Lan House")

        # Configurações da página
        self.root.geometry("1466x768")
        self.root.config(bg="#2c3e50")

        # Título da janela
        self.title_label = tk.Label(self.root, text="Simulador de Lan House", font=("Arial", 24, "bold"), bg="#2c3e50", fg="white")
        self.title_label.pack(pady=20)

        # Informações principais (data e hora)
        self.label_data_hora = tk.Label(self.root, text="", font=("Arial", 16), bg="#2c3e50", fg="white")
        self.label_data_hora.pack(pady=10)

        # Botão iniciar
        self.button_iniciar = tk.Button(self.root, text="Iniciar", font=("Arial", 18), command=self.iniciar, bg="#16a085", fg="white", relief="flat", padx=20, pady=10)
        self.button_iniciar.pack(pady=20)

        # Lista para armazenar os nomes de componentes dos computadores
        self.computadores_labels = []

        # Mapeamento de componentes para exibir nomes amigáveis
        self.mapeamento_componentes = {
            "cpu": "Processador",
            "memoria": "Memória",
            "placa_mae": "Placa Mãe",
            "memoria_ram": "Memória RAM",
            "fonte": "Fonte"
        }

        # Frame de computadores
        self.computadores_frame = tk.Frame(self.root, bg="#2c3e50")
        self.computadores_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Inicializa o programa (com PCs e manutenção)
        self.program = Program(self.atualizar_interface)

    def iniciar(self):
        """Função chamada quando o botão 'Iniciar' é pressionado"""
        print("Botão Iniciar pressionado")  # Depuração

        # Remove o botão iniciar da tela
        self.button_iniciar.pack_forget()

        # Criação dos computadores e componentes
        self.criar_computadores()

        # Atualiza a interface a cada segundo
        self.atualizar_interface()

    def criar_computadores(self):
        """Criação dos computadores e seus componentes"""
        nomes_computadores = ["Computador 1", "Computador 2", "Computador 3"]

        for idx, pc in enumerate(self.program.computadores):
            frame = tk.Frame(self.computadores_frame, borderwidth=2, relief="groove", bg="#ecf0f1", padx=15, pady=20, width=400)
            frame.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")

            # Nome do computador
            tk.Label(frame, text=nomes_computadores[idx], font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=5)

            # Exibe os componentes do PC
            for componente in pc.componentes:
                nome_amigavel = self.mapeamento_componentes.get(componente.id, componente.id)
                label = tk.Label(frame, text=str(componente), font=("Arial", 14), bg="#ecf0f1", anchor="w")
                label.pack(fill="x", pady=5)
                self.computadores_labels.append(label)

            # Botões de manutenção
            buttons_frame = tk.Frame(frame, bg="#ecf0f1")
            buttons_frame.pack(pady=15)

            # Botão Preventiva
            tk.Button(buttons_frame, text="Preventiva (R$ 50)", command=lambda p=pc: self.manutencao_preventiva(p), font=("Arial", 14), bg="#27ae60", fg="white", relief="flat", padx=20, pady=5).pack(side="left", padx=10)
            
            # Botão Corretiva
            tk.Button(buttons_frame, text="Corretiva (R$ 30)", command=lambda p=pc: self.manutencao_corretiva(p), font=("Arial", 14), bg="#e74c3c", fg="white", relief="flat", padx=20, pady=5).pack(side="left")

        # Ajuste da largura das colunas (três computadores na tela)
        for col in range(3):
            self.computadores_frame.grid_columnconfigure(col, weight=1, minsize=200)

    def manutencao_preventiva(self, computador):
        """Função para manutenção preventiva"""
        print(f"Manutenção preventiva iniciada no {computador}")  # Print para depuração
        # Aqui vai a lógica para realizar a manutenção preventiva no computador

    def manutencao_corretiva(self, computador):
        """Função para manutenção corretiva"""
        print(f"Manutenção corretiva iniciada no {computador}")  # Print para depuração
        # Aqui vai a lógica para realizar a manutenção corretiva no computador

    def atualizar_interface(self):
        """Atualiza as informações na interface gráfica"""
        print("Atualizando interface...")  # Depuração

        for idx, pc in enumerate(self.program.computadores):
            for j, componente in enumerate(pc.componentes):
                label = self.computadores_labels[idx * len(pc.componentes) + j]
                label.config(text=str(componente))  # Atualiza o texto com as informações do componente

        # Atualiza a data e hora
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.label_data_hora.config(text=f"Data e Hora: {agora}")

        # Atualiza a interface a cada 1000 ms (1 segundo)
        self.root.after(1000, self.atualizar_interface)

# Inicia a aplicação
if __name__ == "__main__":
    app = App()
    app.root.mainloop()  # Aqui ocorre a execução da interface
