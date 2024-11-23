import customtkinter as ctk
import threading
from main import Program

def center(x, y):
    return (x / 2) - (y / 2)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("CustomTkinter")
        self.geometry("400x600")
        ctk.set_appearance_mode("dark")
        self.resizable(False, False)

        # Label de título
        self.label = ctk.CTkLabel(self, text='LabHouse', width=400, height=40, fg_color='#424279', font=('Arial', 16, 'bold'))
        self.label.place(x=0, y=0)

        # Botão de iniciar
        self.btn = ctk.CTkButton(self, text='Iniciar', width=140, height=28, command=self.iniciar)
        self.btn.place(x=center(400, 140), y=center(600, 28))

        # Texto para exibir dia, hora e computadores
        self.status_text = ctk.CTkLabel(self, text="Status:", font=('Arial', 12), width=400, height=40)
        self.status_text.place(x=0, y=60)

        # Criar instância do programa
        self.program = Program(self.atualizar_interface)

    def iniciar(self):
        # Iniciar o thread para a execução do programa em segundo plano
        thread = threading.Thread(target=self.program.iniciar)
        thread.daemon = True  # O thread será encerrado quando a aplicação fechar
        thread.start()

    def atualizar_interface(self, dia, horas, minutos, pcs):
        # Atualizar o texto na interface com o status dos PCs e tempo
        status_text = f"Dia {dia:02} | {horas:02}h{minutos:02}\n"
        for pc in pcs:
            status_text += f"PC: {pc.id} - Ligado: {pc.ligado}\n"
            for componente in pc.componentes:
                status_text += f"  - Componente: {componente.id} | Quebrado: {componente.quebrado} | Tempo de vida: {componente.tempo_de_vida:.2f} | Custo: {componente.custo}\n"
        self.status_text.configure(text=status_text)
        self.after(500, self.atualizar_interface, dia, horas, minutos, pcs)  # Atualiza a interface a cada 500ms

if __name__ == "__main__":
    app = App()
    app.mainloop()
