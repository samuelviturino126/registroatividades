
import tkinter as tk
from tkinter import messagebox
from conectar import conectar
from telaadm import abrir_tela_admin
from telabolsista import abrir_tela_bolsista

#função de login
def login():
    nome = entrada_nome.get().strip() #strip remove espaços ' '
   

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, tipo FROM usuarios WHERE nomeinst = %s AND senha = %s", (nome, senha))
        usuario = cursor.fetchone()
        conexao.close()

        if usuario:
            messagebox.showinfo("Login", f"Bem-vindo, {usuario[1]}!")
            if usuario[2] == 'admin': #A tela de admin é genérica, todos os admin vão ter acesso na mesma tela e não importa quem está logado, ela é genérica
                abrir_tela_admin()
            else:
                abrir_tela_bolsista(usuario[0], usuario[1]) #Aqui lançamos para a função tela do bolsista qual usuário está acessando essa tela e qual o respectivo id desse usuário
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.") 

# INTERFACE DE LOGIN

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\samuel.viturino126\Desktop\BANCO DE DADOS\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("770x447")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 447,
    width = 770,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    99.0,
    139.0,
    anchor="nw",
    text="Nome:",
    fill="#000000",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    100.0,
    241.0,
    anchor="nw",
    text="Senha:",
    fill="#000000",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    303.0,
    399.0,
    anchor="nw",
    text="Não lembro minha senha",
    fill="#000000",
    font=("Inter", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_1.place(
    x=329.0,
    y=325.0,
    width=113.0,
    height=40.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    434.5,
    256.0,
    image=entry_image_1
)
entrada_senha = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entrada_senha.place(
    x=205.0,
    y=235.0,
    width=459.0,
    height=40.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    434.5,
    154.0,
    image=entry_image_2
)
entrada_nome = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entrada_nome.place(
    x=205.0,
    y=133.0,
    width=459.0,
    height=40.0
)

canvas.create_rectangle(
    100.0,
    58.0,
    670.0,
    85.0,
    fill="#AFAFAF",
    outline="")

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
)
button_2.place(
    x=690.0000010243959,
    y=17.0,
    width=54.833494044958115,
    height=54.833494044958115
)
window.resizable(False, False)
window.mainloop()



