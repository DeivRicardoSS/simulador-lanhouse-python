import customtkinter as ctk

def center(x, y):
    return (x/2)-(y/2)

class App(ctk.CTk):
    def __init__(this):
        super().__init__()
        this.title("CustomTkinter")
        this.geometry("400x600")
        ctk.set_appearance_mode("dark")
        this.resizable(False, False)

        this.label = ctk.CTkLabel(this, text='LabHouse', width=400, height=40, fg_color='#424279', font=('Arial', 16, 'bold'))
        this.label.place(x=0, y=0)

        def button_event():
            print('button pressed')
        
        this.btn = ctk.CTkButton(this, text='Butãum', width=140, height=28, command=button_event)
        this.btn.place(x=center(400, 140), y=center(600, 28))

app = App()
app.mainloop()