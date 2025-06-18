import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import *
from conectar import conectar
from datetime import datetime
from pathlib import Path
from tkinter import messagebox
import psycopg2
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import io


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
            #retangulo do lado direito
            1005.0,
            558.0,
            1375.0,
            777.0,
            fill="#D9D9D9",
            outline="")

        self.canvas_tela_adm.create_rectangle(
            #retangulo do centro
            573.0,
            558.0,
            943.0,
            777.0,
            fill="#D9D9D9",
            outline="")

        self.canvas_tela_adm.create_rectangle(
            #retangulo da esquerda
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
            command=lambda: (self.window_tela_adm.destroy(), TelatividadesADM()),
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
        #botão 4 = relatórios
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
        self.graficos()
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
        subprocess.run(["python", "tela_login_classe.py"])
    
    def graficos(self):
        # Dados do gráfico 
        self.labels = ['A', 'B', 'C', 'D', 'F', 'G', 'H'] #Essas labels vão ser as atividades padrao por setor
        self.sizes = [10, 20, 30, 38, 0.2, 0.5, 1.5] #Vai procurar o setor de cada label nas realizadas e retornar a contagem dos feitos
        self.colors = ['#555555', '#888888', '#AAAAAA', '#CCCCCC'] #cores padrão para o programa (cinza)

        # Cria a figura do gráfico
        fig, ax = plt.subplots(figsize=(3.7, 2.19), dpi=100) 
        ax.pie(self.sizes, labels=self.labels, colors=self.colors, autopct='%1.1f%%', startangle=140)
        ax.axis('equal') #padrão porém posso aumentar

        # Salva a figura em memória como imagem
        buf = io.BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', transparent=True)
        buf.seek(0)

        # Carrega a imagem com PIL
        img = Image.open(buf)
        self.tk_image = ImageTk.PhotoImage(img)

        # Desenha a imagem dentro do canvas (por cima do retângulo)
        self.canvas_tela_adm.create_image(600, 570, anchor='nw', image=self.tk_image)

        plt.close(fig)  # Evita vazamento de memória
    
class TelatividadesADM:
    #caminhos
    def __init__ (self):
        OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = OUTPUT_PATH / "telas_adm" / "tela_atividades" / "build" / "assets" / "frame0"
    #window
        self.windowtela_atividade = Tk()
        self.windowtela_atividade.geometry("770x640")
        self.windowtela_atividade.configure(bg = "#FFFFFF")
        self.windowtela_atividade.resizable(False, False)
    #canvas
        self.canvas_tela_atividade = Canvas(
        self.windowtela_atividade,
        bg = "#FFFFFF",
        height = 640,
        width = 770,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
        self.canvas_tela_atividade.place(x = 0, y = 0)
    #textos
        self.canvas_tela_atividade.create_text( 100.0, 241.0, anchor="nw", text="Descrição:", fill="#000000", font=("Inter", 25 * -1)
        )

        self.canvas_tela_atividade.create_text(
            100.0,
            151.0,
            anchor="nw",
            text="Setor:",
            fill="#000000",
            font=("Inter", 25 * -1)
        )

        self.canvas_tela_atividade.create_text(
            420.0,
            151.0,
            anchor="nw",
            text="Tipo:",
            fill="#000000",
            font=("Inter", 25 * -1)
        )
    #botões
        self.tela_atividade_button_image_1 = PhotoImage(
        file=self.relative_to_assets("button_1.png"))
        self.tela_atividade_button_1 = Button(
            image=self.tela_atividade_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.cadastrar_atividade,
            relief="flat"
        )
        self.tela_atividade_button_1.place(
            x=548.0,
            y=537.0,
            width=119.0,
            height=40.0
        )

        self.tela_atividade_button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.tela_atividade_button_2 = Button(
            image=self.tela_atividade_button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.windowtela_atividade.destroy(), TelaAdministrador()),
            relief="flat"
        )
        self.tela_atividade_button_2.place(
            x=690.0000010243959,
            y=17.0,
            width=54.833494044958115,
            height=54.833494044958115
        )
    #restante
        self.tela_atividade_entry_image_1 = PhotoImage(
        file=self.relative_to_assets("entry_1.png"))
        self.tela_atividade_entry_bg_1 = self.canvas_tela_atividade.create_image(
        383.5,
        121.0,
        image=self.tela_atividade_entry_image_1
    )
        self.nome_nova_atividade = Entry( #aqui é uma entrada de uma única linha
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.nome_nova_atividade.place(
            x=105.0,
            y=101.0,
            width=557.0,
            height=40.0
        )

        self.tela_atividade_entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.tela_atividade_entry_bg_2 = self.canvas_tela_atividade.create_image(
            383.0,
            383.0,
            image=self.tela_atividade_entry_image_2
        )
        self.tela_atividade_entry_2 = Text( #aqui eu estou criando minha área de texto
            bd=0, 
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.tela_atividade_entry_2.place( #aqui eu posiciono a área que o texto vai ficar
            x=105.0,
            y=286.0,
            width=556.0,
            height=194.0
        )

        self.tela_atividade_image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.tela_atividade_image_1 = self.canvas_tela_atividade.create_image(
            223.0,
            206.0,
            image=self.tela_atividade_image_image_1
        )
        #tamanho da combobox igual o da janela acima 
        self.combobox_width = 250
        self.combobox_height = 45

    # coordenadas para centralizar no ponto (223, 206)
        self.combobox_x = 223 - self.combobox_width / 2
        self.combobox_y = 206 - self.combobox_height / 2
        #configuração da combobox
        self.setor_atividade = ttk.Combobox(
            self.windowtela_atividade,
            values=["Processamento Técnico", "Reprografia", "Atendimento", "Selecione"],
            state="readonly"
        )
        self.setor_atividade.current(3)
        #local onde ela vai ficar
        self.setor_atividade.place(x=self.combobox_x, y=self.combobox_y, width=self.combobox_width, height=self.combobox_height)



        self.tela_atividade_image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.tela_atividade_image_2 = self.canvas_tela_atividade.create_image(
            543.0,
            206.0,
            image=self.tela_atividade_image_image_2
        )

        #tamanho da combobox igual o da janela acima 
        self.combobox_width = 250
        self.combobox_height = 45

    # coordenadas para centralizar no ponto (223, 206)
        self.combobox_x2 = 543 - self.combobox_width / 2
        self.combobox_y2 = 206 - self.combobox_height / 2
        #configuração da combobox
        self.tipo_atividade = ttk.Combobox(
            self.windowtela_atividade,
            values=["Horas", "Quantidade", "Selecione"],
            state="readonly"
        )
        self.tipo_atividade.current(2)
        #local onde ela vai ficar
        self.tipo_atividade.place(x=self.combobox_x2, y=self.combobox_y2, width=self.combobox_width, height=self.combobox_height)

        self.canvas_tela_atividade.create_text(
            100.0,
            61.0,
            anchor="nw",
            text="Nova atividade",
            fill="#000000",
            font=("Inter Medium", 25 * -1)
        )

        self.tela_atividade_button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.tela_atividade_button_3 = Button(
            image=self.tela_atividade_button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.tela_atividade_button_3.place(
            x=410.0,
            y=534.0,
            width=122.0,
            height=43.0
        )
        self.windowtela_atividade.mainloop()
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    def cadastrar_atividade(self):
        conexao = conectar()
        self.nome = self.nome_nova_atividade.get()
        self.tipo = self.tipo_atividade.get()
        self.setor = self.setor_atividade.get()
        cursor = conexao.cursor()

        if not self.nome or self.tipo == "Selecione" or not self.tipo or self.setor == "Selecione" or not self.setor:
            messagebox.showerror("Erro!", "Preencha todas as lacunas")
            conexao.close()
        else:
            cursor.execute(
                "INSERT INTO atividades_padrao (nome, tipo, setor) VALUES (%s, %s, %s)",
                (self.nome, self.tipo, self.setor)
            )
            conexao.commit()
            messagebox.showinfo("Feito!", "Atividade Cadastrada!") 
            conexao.close()


if __name__ == "__main__":
    TelaAdministrador()

