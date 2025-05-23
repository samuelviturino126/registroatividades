from pathlib import Path
import psycopg2
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from conectar import conectar
import subprocess

#Para conseguir as atividades do mes e do dia e salvar
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
    window.destroy()
    subprocess.run(["python", "main.py"])

#DESIGN
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "telaadm" / "build" / "assets" / "frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x846")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 846,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    135.0,
    0.0,
    1305.0,
    83.0,
    fill="#F2F2F2",
    outline="")

canvas.create_rectangle(
    335.0,
    158.0,
    705.0,
    377.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    1005.0,
    558.0,
    1375.0,
    777.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    573.0,
    558.0,
    943.0,
    777.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    150.0,
    558.0,
    520.0,
    777.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    735.0,
    158.0,
    1105.0,
    377.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    500.0,
    188.0,
    anchor="nw",
    text= atividades_do_mes,
    fill="#000000",
    font=("Inter Bold", 60 * -1)
)

canvas.create_text(
    232.0,
    468.0,
    anchor="nw",
    text="Últimas atividades registradas",
    fill="#000000",
    font=("Inter Medium", 25 * -1)
)

canvas.create_text(
    899.0,
    188.0,
    anchor="nw",
    text=atividades_do_dia,
    fill="#000000",
    font=("Inter Bold", 60 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: voltar(),
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
    x=830.0,
    y=36.0,
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

canvas.create_text(
    383.0,
    268.0,
    anchor="nw",
    text="Atividades Registradas",
    fill="#000000",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    472.0,
    300.0,
    anchor="nw",
    text="no mês",
    fill="#000000",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    784.0,
    268.0,
    anchor="nw",
    text="Atividades Registradas",
    fill="#000000",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    890.0,
    300.0,
    anchor="nw",
    text="hoje.",
    fill="#000000",
    font=("Inter", 25 * -1)
)
window.resizable(True, True)
window.mainloop()
