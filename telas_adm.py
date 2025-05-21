from pathlib import Path
import psycopg2
from tkinter import * 
from tkinter import ttk
from conectar import conectar
import subprocess
from tkinter import messagebox

#essa função abre a primeira tela
def abrirtelaadm():        
    #Primeira parte é para conseguir as atividades do mes e do dia e salvar
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT COUNT(id)
            FROM atividades_realizadas
            WHERE EXTRACT(MONTH FROM data) = EXTRACT(MONTH FROM CURRENT_DATE)
        """)
        resultado = cursor.fetchone()
        atividades_do_mes = resultado[0] if resultado else 0
        cursor.execute("""
            SELECT COUNT(id)
            FROM atividades_realizadas
            WHERE data::date = CURRENT_DATE
        """)
        resultado = cursor.fetchone()
        atividades_do_dia = resultado[0] if resultado else 0
        conexao.close()
    else:
        atividades_do_mes = "Erro"
        atividades_do_dia = "Erro"

    def voltar():
        window1.destroy()
        subprocess.run(["python", "tela_login.py"])
    
    #DESIGN
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "telas_adm" / "tela_principal" / "build" / "assets" / "frame0"


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window1 = Tk()

    window1.geometry("1440x846")
    window1.configure(bg = "#FFFFFF")


    canvas1 = Canvas(
        window1,
        bg = "#FFFFFF",
        height = 846,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas1.place(x = 0, y = 0)
    canvas1.create_rectangle(
        135.0,
        0.0,
        1305.0,
        83.0,
        fill="#F2F2F2",
        outline="")

    canvas1.create_rectangle(
        335.0,
        158.0,
        705.0,
        377.0,
        fill="#D9D9D9",
        outline="")

    canvas1.create_rectangle(
        1005.0,
        558.0,
        1375.0,
        777.0,
        fill="#D9D9D9",
        outline="")

    canvas1.create_rectangle(
        573.0,
        558.0,
        943.0,
        777.0,
        fill="#D9D9D9",
        outline="")

    canvas1.create_rectangle(
        150.0,
        558.0,
        520.0,
        777.0,
        fill="#D9D9D9",
        outline="")

    canvas1.create_rectangle(
        735.0,
        158.0,
        1105.0,
        377.0,
        fill="#D9D9D9",
        outline="")

    canvas1.create_text(
        500.0,
        188.0,
        anchor="nw",
        text= atividades_do_mes,
        fill="#000000",
        font=("Inter Bold", 60 * -1)
    )

    canvas1.create_text(
        232.0,
        468.0,
        anchor="nw",
        text="Últimas atividades registradas",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    canvas1.create_text(
        899.0,
        188.0,
        anchor="nw",
        text=atividades_do_dia,
        fill="#000000",
        font=("Inter Bold", 60 * -1)
    )

    button_voltar_image = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_voltar = Button(
        image=button_voltar_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: voltar(),
        relief="flat"
    )
    button_voltar.place(
        x=1243.0,
        y=24.0,
        width=34.0,
        height=34.0
    )

    button_image_atividades_adm = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_atividades_adm = Button(
        image=button_image_atividades_adm,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: (window1.destroy(), tela_atividades()),
        relief="flat"
    )
    button_atividades_adm.place(
        x=830.0,
        y=36.0,
        width=90.0,
        height=22.0
    )

    button_image_bolsistas_adm = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_bolsistas_adm = Button(
        image=button_image_bolsistas_adm,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_bolsistas_adm.place(
        x=682.0,
        y=36.0,
        width=76.0,
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
        x=985.0,
        y=21.0,
        width=157.0,
        height=42.0
    )

    canvas1.create_text(
        383.0,
        268.0,
        anchor="nw",
        text="Atividades Registradas",
        fill="#000000",
        font=("Inter", 25 * -1)
    )

    canvas1.create_text(
        472.0,
        300.0,
        anchor="nw",
        text="no mês",
        fill="#000000",
        font=("Inter", 25 * -1)
    )

    canvas1.create_text(
        784.0,
        268.0,
        anchor="nw",
        text="Atividades Registradas",
        fill="#000000",
        font=("Inter", 25 * -1)
    )

    canvas1.create_text(
        890.0,
        300.0,
        anchor="nw",
        text="hoje.",
        fill="#000000",
        font=("Inter", 25 * -1)
    )
    window1.resizable(True, True)
    window1.mainloop()

def tela_atividades():
    conexao = conectar()
    def cadastrar_atividade():
        nome = nome_nova_atividade.get()
        tipo = tipo_atividade.get()
        setor = setor_atividade.get()
        cursor = conexao.cursor()
        if not nome or tipo == "Selecione" or not tipo or setor == "Selecione" or not setor:
            cursor.execute("INSERT INTO atividades_padrao (nome, tipo, setor) VALUES (%s, %s, %s)", (nome, tipo, setor))
            messagebox.showerror("Erro!","Preencha todas as lacunas")
            conexao.close()
        else:
            conexao.commit()
            messagebox.showinfo("Feito!", "Atividade Cadastrada!") 
            conexao.close()

    #DESIGN
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\samuel.viturino126\Desktop\BANCODEDADOS_ORGANIZAR\telas_adm\tela_atividades\build\assets\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    windowtela_atividade = Tk()

    windowtela_atividade.geometry("770x640")
    windowtela_atividade.configure(bg = "#FFFFFF")


    canvas_tela_atividade = Canvas(
        windowtela_atividade,
        bg = "#FFFFFF",
        height = 640,
        width = 770,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas_tela_atividade.place(x = 0, y = 0)
    canvas_tela_atividade.create_text(
        100.0,
        241.0,
        anchor="nw",
        text="Descrição:",
        fill="#000000",
        font=("Inter", 25 * -1)
    )

    canvas_tela_atividade.create_text(
        100.0,
        151.0,
        anchor="nw",
        text="Setor:",
        fill="#000000",
        font=("Inter", 25 * -1)
    )

    canvas_tela_atividade.create_text(
        420.0,
        151.0,
        anchor="nw",
        text="Tipo:",
        fill="#000000",
        font=("Inter", 25 * -1)
    )

    tela_atividade_button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    tela_atividade_button_1 = Button(
        image=tela_atividade_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=cadastrar_atividade,
        relief="flat"
    )
    tela_atividade_button_1.place(
        x=548.0,
        y=537.0,
        width=119.0,
        height=40.0
    )

    tela_atividade_button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    tela_atividade_button_2 = Button(
        image=tela_atividade_button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    tela_atividade_button_2.place(
        x=690.0000010243959,
        y=17.0,
        width=54.833494044958115,
        height=54.833494044958115
    )

    tela_atividade_entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    tela_atividade_entry_bg_1 = canvas_tela_atividade.create_image(
        383.5,
        121.0,
        image=tela_atividade_entry_image_1
    )
    nome_nova_atividade = Entry( #aqui é uma entrada de uma única linha
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    nome_nova_atividade.place(
        x=105.0,
        y=101.0,
        width=557.0,
        height=40.0
    )

    tela_atividade_entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    tela_atividade_entry_bg_2 = canvas_tela_atividade.create_image(
        383.0,
        383.0,
        image=tela_atividade_entry_image_2
    )
    tela_atividade_entry_2 = Text( #aqui eu estou criando minha área de texto
        bd=0, 
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    tela_atividade_entry_2.place( #aqui eu posiciono a área que o texto vai ficar
        x=105.0,
        y=286.0,
        width=556.0,
        height=194.0
    )

    tela_atividade_image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    tela_atividade_image_1 = canvas_tela_atividade.create_image(
        223.0,
        206.0,
        image=tela_atividade_image_image_1
    )
    #tamanho da combobox igual o da janela acima 
    combobox_width = 250
    combobox_height = 45

# coordenadas para centralizar no ponto (223, 206)
    combobox_x = 223 - combobox_width / 2
    combobox_y = 206 - combobox_height / 2
    #configuração da combobox
    setor_atividade = ttk.Combobox(
        windowtela_atividade,
        values=["Processamento Técnico", "Reprografia", "Atendimento", "Selecione"],
        state="readonly"
    )
    setor_atividade.current(3)
    #local onde ela vai ficar
    setor_atividade.place(x=combobox_x, y=combobox_y, width=combobox_width, height=combobox_height)



    tela_atividade_image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    tela_atividade_image_2 = canvas_tela_atividade.create_image(
        543.0,
        206.0,
        image=tela_atividade_image_image_2
    )

    #tamanho da combobox igual o da janela acima 
    combobox_width = 250
    combobox_height = 45

# coordenadas para centralizar no ponto (223, 206)
    combobox_x2 = 543 - combobox_width / 2
    combobox_y2 = 206 - combobox_height / 2
    #configuração da combobox
    tipo_atividade = ttk.Combobox(
        windowtela_atividade,
        values=["Horas", "Quantidade", "Selecione"],
        state="readonly"
    )
    tipo_atividade.current(2)
    #local onde ela vai ficar
    tipo_atividade.place(x=combobox_x2, y=combobox_y2, width=combobox_width, height=combobox_height)

    canvas_tela_atividade.create_text(
        100.0,
        61.0,
        anchor="nw",
        text="Nova atividade",
        fill="#000000",
        font=("Inter Medium", 25 * -1)
    )

    tela_atividade_button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    tela_atividade_button_3 = Button(
        image=tela_atividade_button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    tela_atividade_button_3.place(
        x=410.0,
        y=534.0,
        width=122.0,
        height=43.0
    )
    windowtela_atividade.resizable(False, False)
    windowtela_atividade.mainloop()
abrirtelaadm()
