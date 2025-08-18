import tkinter as tk
from tkinter import Toplevel, Listbox, PhotoImage, StringVar

class ComboboxComImagem:
    def __init__(self, root):
        self.root = root
        self.root.title("Combobox com Imagem")
        self.root.geometry("400x300")

        # Variável para armazenar a opção selecionada
        self.selected_option = StringVar()
        self.selected_option.set("Selecione")  # Valor padrão

        # Carregar a imagem que simula a combobox (use sua imagem real)
        self.button_image = PhotoImage(file="button_2.png")  # substitua com seu caminho

        # Botão com imagem (simula o componente visual)
        self.combo_button = tk.Button(
            self.root,
            image=self.button_image,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=self.show_dropdown  # chama o menu ao clicar
        )
        self.combo_button.place(x=100, y=50, width=150, height=30)

        # Texto da opção selecionada, sobreposto ao botão
        self.text_label = tk.Label(
            self.root,
            textvariable=self.selected_option,
            bg="#ffffff",  # fundo igual ao da imagem
            fg="black",
            font=("Arial", 10),
            anchor="w"
        )
        self.text_label.place(x=110, y=55, width=130)

    def show_dropdown(self):
        # Cria um popup tipo menu suspenso
        self.popup = Toplevel(self.root)
        self.popup.overrideredirect(True)  # remove barra de título e bordas

        # Calcula posição: logo abaixo do botão
        x = self.combo_button.winfo_rootx()
        y = self.combo_button.winfo_rooty() + self.combo_button.winfo_height()

        # Define o tamanho e posição do popup
        self.popup.geometry(f"150x90+{x}+{y}")  # largura igual ao botão

        # Cria a lista de opções
        options = ["Processamento Técnico", "Reprografia", "Atendimento"]
        self.listbox = Listbox(
            self.popup,
            font=("Arial", 10),
            height=len(options),
            exportselection=False
        )

        # Adiciona as opções na lista
        for option in options:
            self.listbox.insert(tk.END, option)

        self.listbox.pack(fill="both", expand=True)

        # Detecta seleção de item
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        # Fecha o popup se perder o foco (clicar fora)
        self.popup.bind("<FocusOut>", lambda e: self.popup.destroy())
        self.popup.focus_force()

    def on_select(self, event):
        # Pega a opção selecionada
        selection = self.listbox.get(self.listbox.curselection())
        self.selected_option.set(selection)
        print(f"Opção selecionada: {selection}")

        # Fecha o popup
        self.popup.destroy()

# Execução
if __name__ == "__main__":
    root = tk.Tk()
    app = ComboboxComImagem(root)
    root.mainloop()
