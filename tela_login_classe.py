from conectar import conectar
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from pathlib import Path
from tela_adm_classe import TelaAdministrador
from tela_bolsistas_classe import TelaBolsista

fonte_personalizada = ("Arial", 14, "bold")
class TelaLogin:
    def __init__(self):
        # Caminhos
        OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = OUTPUT_PATH / "tela_login" / "build" / "assets" / "frame0"
        # Janela principal
        self.window = Tk()
        self.window.geometry("770x447")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)
        self.window.title("Login")
        # Canvas
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=447,
            width=770,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        # Texto
        self.canvas.create_text(99, 139, anchor="nw", text="Nome:", fill="#000", font=("Inter", 25 * -1))
        self.canvas.create_text(100, 241, anchor="nw", text="Senha:", fill="#000", font=("Inter", 25 * -1))
        self.canvas.create_text(303, 399, anchor="nw", text="Não lembro minha senha", fill="#000", font=("Inter", 14 * -1))
        self.canvas.create_rectangle(100, 58, 670, 85, fill="#AFAFAF", outline="")

        # Entradas
        self.entry_nome_img = PhotoImage(file=self.relative_to_assets("entry_login_2.png"))
        self.canvas.create_image(434.5, 154.0, image=self.entry_nome_img)
        self.entrada_nome = Entry(bd=0, bg="#D9D9D9", fg="#000716", font=fonte_personalizada, highlightthickness=0)
        self.entrada_nome.place(x=205, y=133, width=459, height=40)

        self.entry_senha_img = PhotoImage(file=self.relative_to_assets("entry_login.png"))
        self.canvas.create_image(434.5, 256.0, image=self.entry_senha_img)
        self.entrada_senha = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0, show="*")
        self.entrada_senha.place(x=205, y=235, width=459, height=40)

        # Botões
        self.button_login_img = PhotoImage(file=self.relative_to_assets("button_login.png"))
        self.button_login = Button(image=self.button_login_img, borderwidth=0, highlightthickness=0,
                                   command=self.login, relief="flat")
        self.button_login.place(x=329, y=325, width=113, height=40)

        self.button_fechar_img = PhotoImage(file=self.relative_to_assets("button_fechar_login.png"))
        self.button_fechar = Button(image=self.button_fechar_img, borderwidth=0, highlightthickness=0,
                                    command=self.window.destroy, relief="flat")
        self.button_fechar.place(x=690, y=17, width=54.8, height=54.8)

        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def login(self):
        nome = self.entrada_nome.get().strip()
        senha = self.entrada_senha.get()

        conexao = conectar()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome, tipo FROM usuarios WHERE nomeinst = %s AND senha = %s", (nome, senha))
            usuario = cursor.fetchone()
            conexao.close()

            if usuario:
                messagebox.showinfo("Login", f"Bem-vindo, {usuario[1]}!")
                self.window.destroy()
                if usuario[2] == 'admin':
                    TelaAdministrador()
                else:
                    TelaBolsista(usuario[0], usuario[1])
            else:
                messagebox.showerror("Erro", "Usuário ou senha incorretos.")
if __name__ == "__main__":
    TelaLogin()
