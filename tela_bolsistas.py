from pathlib import Path
import psycopg2
from tkinter import * 
from tkinter import ttk
from conectar import conectar
import subprocess
from tkinter import messagebox

#Função para mostrar as atividades cadastradas
def abrir_tela_bolsista():
    def selecionar_atividades():
        campo_atividade_selecionada = campo_selecionada.get()
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO atividade_por_usuarios (usuario_id, atividade_id) VALUES (%s, %s) ON CONFLICT (usuario_id, atividade_id) DO NOTHING;",(id, campo_atividade_selecionada))
        conexao.commit()
        conexao.close()


    #def cadastrar_atividade_bolsista():
      #  conexao = conectar()
      #  nome_atividade = atividade_desempenhada.get() #nome da atividade
      #  data = data_atividade.get() #data da atividade
      #  quantidade = quantidade_atividade.get() #quantidade atividade
       # cursor = conexao.cursor()
       # if not nome or not data or not quantidade:
       #     cursor.execute("INSERT INTO atividades_realizadas (nome, tipo, setor) VALUES (%s, %s, %s)", (nome, tipo, setor))
      #      messagebox.showerror("Erro!","Preencha todas as lacunas")
       #     conexao.close()
       # else:
       #     conexao.commit()
        #    messagebox.showinfo("Feito!", "Atividade Cadastrada!") 
        #    conexao.close()
       # pass
    
    #design da tela de bolsista
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH  / "telas_bolsistas" / "tela_principal" / "build" / "assets" / "frame0"


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window_tela_bolsista = Tk()

    window_tela_bolsista.geometry("1440x846")
    window_tela_bolsista.configure(bg = "#FFFFFF")


    canvas_tela_bolsista = Canvas(
        window_tela_bolsista,
        bg = "#FFFFFF",
        height = 846,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas_tela_bolsista.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas_tela_bolsista.create_image(
        720.0,
        41.0,
        image=image_image_1
    )

    canvas_tela_bolsista.create_rectangle(
        335.0,
        158.0,
        705.0,
        377.0,
        fill="#D9D9D9",
        outline="")

    canvas_tela_bolsista.create_text(
        232.0,
        537.0,
        anchor="nw",
        text="Últimas atividades registradas",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas_tela_bolsista.create_rectangle(
        735.0,
        158.0,
        1105.0,
        377.0,
        fill="#D9D9D9",
        outline="")

    canvas_tela_bolsista.create_rectangle(
        237.0,
        591.0,
        1205.0,
        630.0,
        fill="#D9D9D9",
        outline="")

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas_tela_bolsista.create_image(
        721.0,
        663.0,
        image=image_image_2
    )

    canvas_tela_bolsista.create_rectangle(
        237.0,
        697.0,
        1205.0,
        736.0,
        fill="#D9D9D9",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=1243.0,
        y=24.0,
        width=34.0,
        height=34.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=723.0,
        y=30.0,
        width=90.0,
        height=22.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=877.0,
        y=30.0,
        width=80.0,
        height=22.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=1013.0,
        y=21.0,
        width=184.0,
        height=42.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas_tela_bolsista.create_image(
        520.0,
        318.0,
        image=entry_image_1
    )
    entry_1 = Text(
        bd=0,
        bg="#000000",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=384.0,
        y=288.0,
        width=272.0,
        height=58.0
    )

    canvas_tela_bolsista.create_text(
        505.0,
        188.0,
        anchor="nw",
        text="3",
        fill="#000000",
        font=("Inter Bold", 60 * -1)
    )

    canvas_tela_bolsista.create_text(
        905.0,
        188.0,
        anchor="nw",
        text="2",
        fill="#000000",
        font=("Inter Bold", 60 * -1)
    )

    canvas_tela_bolsista.create_text(
        784.0,
        286.0,
        anchor="nw",
        text="Atividades Registradas\nHoje",
        fill="#000000",
        font=("Inter", 25 * -1)
    )
    window_tela_bolsista.resizable(False, False)
    window_tela_bolsista.mainloop()


abrir_tela_bolsista()
