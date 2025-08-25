from tkinter import *
from tkinter import ttk

class TelaBolsista():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.window_tela_principalb = Tk()
        self.window_tela_principalb.geometry("1440x846")
        self.window_tela_principalb.configure(bg="#FFFFFF")
        self.window_tela_principalb.resizable(False, False)

        # Título
        label_titulo = Label(self.window_tela_principalb, 
                             text="Últimas atividades registradas", 
                             font=("Inter Medium", 25),
                             bg="#FFFFFF")
        label_titulo.place(x=232, y=537)

        # Criando frame com scrollbar
        container = Frame(self.window_tela_principalb, bg="#FFFFFF")
        container.place(x=230, y=580, width=900, height=200)  # altura para caber 3 cartões

        canvas = Canvas(container, bg="#FFFFFF")
        scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
        scroll_frame = Frame(canvas, bg="#FFFFFF")

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Criar 10 quadrados de exemplo
        for i in range(10):
            card = Frame(scroll_frame, bg="#D9D9D9", width=850, height=50)
            card.pack(pady=5)

            label = Label(card, text=f"Atividade {i+1}", bg="#D9D9D9", font=("Inter", 14))
            label.place(relx=0.5, rely=0.5, anchor="center")

        self.window_tela_principalb.mainloop()


if __name__ == "__main__":
    TelaBolsista(1, "Samuel")