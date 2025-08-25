import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import *
from conectar import conectar
from datetime import datetime
from pathlib import Path
from tkinter import messagebox
import psycopg2
from tkcalendar import DateEntry
from datetime import datetime, date


class TelaBolsista():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        #CAMINHOS
        OUTPUT_PATH = Path(__file__).parent.parent
        self.ASSETS_PATH = OUTPUT_PATH / "telas_bolsistas" / "tela_principal" / "build" / "assets" / "frame0"
        self.window_tela_principalb = Tk()
        self.window_tela_principalb.geometry("1440x846")
        self.window_tela_principalb.configure(bg = "#FFFFFF")
        self.window_tela_principalb.resizable(False,False)
        self.canvas_principalb = Canvas(
            self.window_tela_principalb,
            bg = "#FFFFFF",
            height = 846,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas_principalb.place(x = 0, y = 0)
        #TEXTOS
        
        self.image_image_1 = PhotoImage(
        file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas_principalb.create_image(
            720.0,
            41.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas_principalb.create_image(
            269.0,
            41.0,
            image=self.image_image_2
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=1005.0,
            y=21.0,
            width=184.0,
            height=42.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=725.0,
            y=30.0,
            width=80.0,
            height=22.0
        )

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=860.0,
            y=30.0,
            width=90.0,
            height=22.0
        )

        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=1243.0,
            y=24.0,
            width=34.0,
            height=34.0
        )

        self.button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.window_tela_principalb.destroy(), TelaRegistrar(self.id, self.nome)),
            relief="flat"
        )
        self.button_5.place(
            x=628.0,
            y=436.0,
            width=184.0,
            height=42.0
        )

        self.canvas_principalb.create_rectangle(
            335.0,
            158.0,
            705.0,
            377.0,
            fill="#D9D9D9",
            outline="")

        self.canvas_principalb.create_text(
            477.0,
            316.0,
            anchor="nw",
            text="no mês",
            fill="#000000",
            font=("Inter", 25 * -1)
        )

        self.canvas_principalb.create_text(
            505.0,
            188.0,
            anchor="nw",
            text="3",
            fill="#000000",
            font=("Inter Bold", 60 * -1)
        )

        self.canvas_principalb.create_text(
            384.0,
            288.0,
            anchor="nw",
            text="Atividades registradas",
            fill="#000000",
            font=("Inter", 25 * -1)
        )

        self.canvas_principalb.create_text(
            232.0,
            537.0,
            anchor="nw",
            text="Últimas atividades registradas",
            fill="#000000",
            font=("Inter Medium", 25 * -1)
        )

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas_principalb.create_image(
            721.0,
            610.0,
            image=self.image_image_3
        )

        self.canvas_principalb.create_rectangle(
            735.0,
            158.0,
            1105.0,
            377.0,
            fill="#D9D9D9",
            outline="")

        self.canvas_principalb.create_text(
            894.0,
            312.0,
            anchor="nw",
            text="hoje",
            fill="#000000",
            font=("Inter", 25 * -1)
        )

        self.canvas_principalb.create_text(
            905.0,
            188.0,
            anchor="nw",
            text="2",
            fill="#000000",
            font=("Inter Bold", 60 * -1)
        )

        self.canvas_principalb.create_text(
            784.0,
            288.0,
            anchor="nw",
            text="Atividades registradas ",
            fill="#000000",
            font=("Inter", 25 * -1)
        )
        self.window_tela_principalb.mainloop()
    def relative_to_assets(self, path: str) -> Path:
            return self.ASSETS_PATH / Path(path)
    def selecionar_atividades(self):
        #essa função busca o nome das atividades pela tabela de atividades por usuarios
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT ap.nome
            FROM atividade_por_usuarios AS au
            JOIN atividades_padrao AS ap ON au.atividade_id = ap.id
            WHERE au.usuario_id = %s;
        """, (self.id, ))
        self.dados = [linha[0] for linha in cursor.fetchall()]
        conexao.close()
    def atividades_do_dia_bolsista(self):
        pass
    def atividades_do_mes_bolsista(self):
        pass
    def ultimas_atividades_registradas(self):
        #VOU PRECISAR APENAS DAS ÚLTIMAS 3 atividades
        pass

class TelaRegistrar():
    def __init__(self,id,nome):
        OUTPUT_PATH = Path(__file__).parent.parent
        self.ASSETS_PATH = OUTPUT_PATH / "telas_bolsistas" / "tela_registros" / "build" / "assets" / "frame0"
        self.id = id
        self.nome = nome
        conexao = conectar()
        cursor = conexao.cursor()
        #essa função coleta os id's de cada atividade associada a cada bolsista
        cursor.execute("""
            SELECT ap.nome
            FROM atividade_por_usuarios AS au
            JOIN atividades_padrao AS ap ON au.atividade_id = ap.id
            WHERE au.usuario_id = %s;
        """, (self.id, ))
        self.dados = [linha[0] for linha in cursor.fetchall()] 
        conexao.close()
        #tela
        self.window_telaregistrar = Tk()
        self.window_telaregistrar.geometry("770x447")
        self.window_telaregistrar.configure(bg = "#FFFFFF")
        self.window_telaregistrar.resizable(False, False)
        #canvas
        self.canvas_telaregistrar = Canvas(
            self.window_telaregistrar,
            bg = "#FFFFFF",
            height = 447,
            width = 770,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas_telaregistrar.place(x = 0, y = 0)
        self.canvas_telaregistrar.create_text(
            100.0,
            115.0,
            anchor="nw",
            text="Atividade desempenhada: ",
            fill="#000000",
            font=("Inter", 25 * -1)
            )
        #textos
        self.canvas_telaregistrar.create_text(
            100.0,
            216.0,
            anchor="nw",
            text="Data:",
            fill="#000000",
            font=("Inter", 25 * -1)
        )

        self.canvas_telaregistrar.create_text(
            493.0,
            216.0,
            anchor="nw",
            text="Quantidade:",
            fill="#000000",
            font=("Inter", 25 * -1)
        )
        #Botões
        self.button_image_1 = PhotoImage(
        file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.registrar_atividade_bolsista(),
            relief="flat"
        )
        self.button_1.place(
            x=551.0,
            y=337.0,
            width=119.0,
            height=40.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=437.0,
            y=337.0,
            width=99.0,
            height=40.0
        )
        #entradas
        #ESsa entrada é a da DATA
        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas_telaregistrar.create_image(
            235.5,
            276.0,
            image=self.entry_image_1
        )
        self.entry_data = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_data.place(
            x=105.0,
            y=255.0,
            width=261.0,
            height=40.0
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas_telaregistrar.create_image(
            581.5,
            276.0,
            image=self.entry_image_2
        )
        self.entry_quantidade = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_quantidade.place(
            x=498.0,
            y=255.0,
            width=167.0,
            height=40.0
        )
        #alterar os valores para receber das atiidades por usuarios
        self.atividade = ttk.Combobox(
            self.window_telaregistrar,
            values= self.dados,
            state="readonly"
        )
        self.atividade.place(
            x=105.0,
            y=154.0,
            width=568.0,
            height=40.0
            )

        #retangulos
        self.canvas_telaregistrar.create_rectangle(
            100.0,
            58.0,
            670.0,
            85.0,
            fill="#AFAFAF",
            outline="")

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.window_telaregistrar.destroy(), TelaBolsista(self.id, self.nome)),
            relief="flat"
        )
        self.button_3.place(
            x=690.0000010243959,
            y=17.0,
            width=54.833494044958115,
            height=54.833494044958115
        )
        self.window_telaregistrar.mainloop()

    def relative_to_assets(self, path: str) -> Path:
            return self.ASSETS_PATH / Path(path)
        
    def registrar_atividade_bolsista(self):
        self.atividade_feita = self.atividade.get()
        self.quantidade = self.entry_quantidade.get()   
        self.data = self.entry_data.get()
        from datetime import datetime
        formatos_aceitos = ["%d/%m/%Y", "%d-%m-%Y"]
        self.data_str = self.entry_data.get()
        self.data = None
        for formato in formatos_aceitos:
            try:
                self.data = datetime.strptime(self.data_str, formato).date()
                break  # para no primeiro formato que der certo
            except ValueError:
                continue
        if self.data is None:
            messagebox.showerror("Erro de Data", "Formato inválido. Use DD/MM/AAAA ou DD-MM-AAAA.")
            return
        if self.data > date.today():
            messagebox.showerror("Erro de Data", "Não é permitido registrar uma atividade com data futura.")
            return

        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT id
            FROM atividades_padrao
            WHERE nome = %s;
            """, (self.atividade_feita,)) #aqui nos obtemos o ID pelo nome da atividade
        resultado_id = cursor.fetchone()
        self.id_atividade = resultado_id[0]
        cursor.execute("SELECT setor FROM atividades_padrao WHERE id = %s;", (self.id_atividade, )) #Aqui obtemos o setor da atividade pelo ID
        resultado_setor = cursor.fetchone()
        self.setor_atividade = resultado_setor[0]
        cursor.execute("INSERT INTO atividades_realizadas (usuario_id, atividade_id, data, inteiro, setor) VALUES (%s, %s, %s, %s, %s)", (self.id, self.id_atividade, self.data, self.quantidade, self.setor_atividade))
        conexao.commit()
        conexao.close()













 #class TelaRegistros():
 #   def __init__(self,id,nome):
 #       self.id = id
  #      self.nome = nome
  #      #tela
  #      pass
  #  def registros_bolsista(self):
  #      conexao = conectar()
  #      cursor = conexao.cursor()
  #      cursor.execute("""SELECT * FROM
  #                        atividades_realizadas
  #                        WHERE usuario_id = %s""", self.id)
   #     self.registros = cursor.fetchall()
  #      pass

        
        
        
        




