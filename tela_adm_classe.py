import subprocess
import tkinter as tk
from tkinter import Tk, Canvas, PhotoImage, Button, Entry
from conectar import conectar
from datetime import datetime
from pathlib import Path

class TelaAdministrador:
    def __init__(self):
        #caminhos
        OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = OUTPUT_PATH / "telas_adm" / "tela_principal" / "build" / "assets" / "frame0"
        #janela principal
        self.window_tela_adm = Tk()
        self.window_tela_adm.geometry("1440x846")
        self.window_tela_adm.configure(bg = "#FFFFFF")
        self.window_tela_adm.resizable(False, False)
        self.window_tela_adm.title("Tela_ADM")
        #canvas
        self.canvas_tela_adm = Canvas(
        self.window_tela_adm,
        bg = "#FFFFFF",
        height = 846,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
        self.coletar_dados_adm()
        self.canvas_tela_adm.place(x = 0, y = 0)
        #retangulos
        self.canvas_tela_adm.create_rectangle(
        135.0,
        0.0,
        1305.0,
        83.0,
        fill="#F2F2F2",
        outline="")

        self.canvas_tela_adm.create_rectangle(
            335.0,
            158.0,
            705.0,
            377.0,
            fill="#D9D9D9",
            outline="")

        self.canvas_tela_adm.create_rectangle(
            1005.0,
            558.0,
            1375.0,
            777.0,
            fill="#D9D9D9",
            outline="")

        self.canvas_tela_adm.create_rectangle(
            573.0,
            558.0,
            943.0,
            777.0,
            fill="#D9D9D9",
            outline="")

        self.canvas_tela_adm.create_rectangle(
            150.0,
            558.0,
            520.0,
            777.0,
            fill="#D9D9D9",
            outline="")

        self.canvas_tela_adm.create_rectangle(
            735.0,
            158.0,
            1105.0,
            377.0,
            fill="#D9D9D9",
            outline="")
        #TEXTOS
        self.canvas_tela_adm.create_text(
        500.0,
        188.0,
        anchor="nw",
        text= self.atividades_do_mes,
        fill="#000000",
        font=("Inter Bold", 60 * -1)
    )

        self.canvas_tela_adm.create_text(
            232.0,
            468.0,
            anchor="nw",
            text="Últimas atividades registradas",
            fill="#000000",
            font=("Inter Medium", 25 * -1)
        )

        self.canvas_tela_adm.create_text(
            899.0,
            188.0,
            anchor="nw",
            text=self.atividades_do_dia,
            fill="#000000",
            font=("Inter Bold", 60 * -1)
        )
        self.canvas_tela_adm.create_text(
            383.0,
            268.0,
            anchor="nw",
            text="Atividades Registradas",
            fill="#000000",
            font=("Inter", 25 * -1)
        )

        self.canvas_tela_adm.create_text(
            472.0,
            300.0,
            anchor="nw",
            text="no mês",
            fill="#000000",
            font=("Inter", 25 * -1)
        )

        self.canvas_tela_adm.create_text(
            784.0,
            268.0,
            anchor="nw",
            text="Atividades Registradas",
            fill="#000000",
            font=("Inter", 25 * -1)
        )

        self.canvas_tela_adm.create_text(
            890.0,
            300.0,
            anchor="nw",
            text="hoje.",
            fill="#000000",
            font=("Inter", 25 * -1)
        )
        #Botões
        self.button_voltar_image = PhotoImage(
        file=self.relative_to_assets("button_voltar_adm.png"))
        self.button_voltar = Button(
            image=self.button_voltar_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.voltar(),
            relief="flat"
        )
        self.button_voltar.place(
            x=1243.0,
            y=24.0,
            width=34.0,
            height=34.0
        )

        self.button_image_atividades_adm = PhotoImage(
            file=self.relative_to_assets("button_atividades_adm.png"))
        self.button_atividades_adm = Button(
            image=self.button_image_atividades_adm,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.window_tela_adm.destroy(), self.tela_atividades()),
            relief="flat"
        )
        self.button_atividades_adm.place(
            x=830.0,
            y=36.0,
            width=90.0,
            height=22.0
        )

        self.button_image_bolsistas_adm = PhotoImage(
            file=self.relative_to_assets("button_bolsistas_adm.png"))
        self.button_bolsistas_adm = Button(
            image=self.button_image_bolsistas_adm,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_bolsistas_adm.place(
            x=682.0,
            y=36.0,
            width=76.0,
            height=22.0
        )

        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_relatorios_adm.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=985.0,
            y=21.0,
            width=157.0,
            height=42.0
        )
        self.window_tela_adm.mainloop()
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    def coletar_dados_adm(self):
        conexao = conectar()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT COUNT(id)
                FROM atividades_realizadas
                WHERE EXTRACT(MONTH FROM data) = EXTRACT(MONTH FROM CURRENT_DATE)
            """)
            resultado = cursor.fetchone()
            self.atividades_do_mes = resultado[0] if resultado else 0
            cursor.execute("""
                SELECT COUNT(id)
                FROM atividades_realizadas
                WHERE data::date = CURRENT_DATE
            """)
            resultado = cursor.fetchone()
            self.atividades_do_dia = resultado[0] if resultado else 0
            conexao.close()
        else:
            self.atividades_do_mes = "Erro"
            self.atividades_do_dia = "Erro"
    def voltar(self):
        self.window_tela_adm.destroy()
        subprocess.run(["python", "tela_login.py"])
    

if __name__ == "__main__":
    TelaAdministrador()

