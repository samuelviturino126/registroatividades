from conectar import conectar #note que como estou importando a função conectar de um arquivo que sempre abre ela, ela vai executar assim que eu iniciar esse programa
import sys
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from telas_adm import *
from tela_bolsistas import *

#Função de login
def login():
    nome = entrada_nome_login.get().strip() #strip remove espaços ' ' e entrada_nome.get() recebe o texto que está em entrada_nome definido mais abaixo
    senha = entrada_senha.get() #o mesmo para o de cima

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, tipo FROM usuarios WHERE nomeinst = %s AND senha = %s", (nome, senha))
        usuario = cursor.fetchone()
        conexao.close()

        if usuario:
            messagebox.showinfo("Login", f"Bem-vindo, {usuario[1]}!")
            if usuario[2] == 'admin': #A tela de admin é genérica, todos os admin vão ter acesso na mesma tela e não importa quem está logado, ela é genérica
                window_login.destroy()
                abrirtelaadm()
            else:
                window_login.destroy()
                abrir_tela_bolsista(usuario[0], usuario[1])
                
                 #Aqui lançamos para a função tela do bolsista qual usuário está acessando essa tela e qual o respectivo id desse usuário")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.") 

# INTERFACE DE LOGIN, é padrão da API que estou utilizando
            
OUTPUT_PATH = Path(__file__).parent #acessamos a pasta onde esse código está
ASSETS_PATH = OUTPUT_PATH / "tela_login" / "build" / "assets" / "frame0" #acessa os arquivos do design


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window_login = Tk()

window_login.geometry("770x447")
window_login.configure(bg = "#FFFFFF")


canvas_login = Canvas(
    window_login,
    bg = "#FFFFFF",
    height = 447,
    width = 770,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas_login.place(x = 0, y = 0)
canvas_login.create_text(
    99.0,
    139.0,
    anchor="nw",
    text="Nome:",
    fill="#000000",
    font=("Inter", 25 * -1)
)

canvas_login.create_text(
    100.0,
    241.0,
    anchor="nw",
    text="Senha:",
    fill="#000000",
    font=("Inter", 25 * -1)
)

canvas_login.create_text(
    303.0,
    399.0,
    anchor="nw",
    text="Não lembro minha senha",
    fill="#000000",
    font=("Inter", 14 * -1)
)

button_image_login_login = PhotoImage(
    file=relative_to_assets("button_login.png"))
button_login_login = Button(
    image=button_image_login_login,
    borderwidth=0,
    highlightthickness=0,
    command=login,
    relief="flat"
)
button_login_login.place(
    x=329.0,
    y=325.0,
    width=113.0,
    height=40.0
)

entry_senha_login = PhotoImage(
    file=relative_to_assets("entry_login.png"))
entry_bg_1_login = canvas_login.create_image(
    434.5,
    256.0,
    image=entry_senha_login
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

entry_nome_login = PhotoImage(
    file=relative_to_assets("entry_login_2.png"))
entry_bg_2_login = canvas_login.create_image(
    434.5,
    154.0,
    image=entry_nome_login
)
entrada_nome_login = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entrada_nome_login.place(
    x=205.0,
    y=133.0,
    width=459.0,
    height=40.0
)

canvas_login.create_rectangle(
    100.0,
    58.0,
    670.0,
    85.0,
    fill="#AFAFAF",
    outline="")

button_fechar_login_image = PhotoImage(
    file=relative_to_assets("button_fechar_login.png"))
button_fechar_login = Button(
    image=button_fechar_login_image,
    borderwidth=0,
    highlightthickness=0,
    command=window_login.destroy,
    relief="flat"
)
button_fechar_login.place(
    x=690.0000010243959,
    y=17.0,
    width=54.833494044958115,
    height=54.833494044958115
)
window_login.resizable(False, False)
window_login.mainloop()
