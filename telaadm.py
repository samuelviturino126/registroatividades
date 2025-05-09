import tkinter as tk
from tkinter import messagebox
from conectar import conectar

#CRIAÇÃO DA DEFINIÇÃO DA TELA DE ADMINISTRADOR
def abrir_tela_admin():
    admin_janela = tk.Toplevel()
    admin_janela.title("Portal do ADM")

    texto_resultado = tk.Text(admin_janela, height=20, width=60)
    texto_resultado.pack()
#FUNÇÃO PARA CARREGAR OS REGISTROS DENTRO DA TELA DE ADM
    def carregar_registros():
        #A CHAMADA DA FUNÇÃO CONECTAR É NECESSARIA PARA ABRIR O SERVIDOR SQL
        conexao = conectar()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT u.nome, a.nome, ar.data, ar.horas
                FROM atividades_realizadas ar
                JOIN usuarios u ON ar.usuario_id = u.id
                JOIN atividades_padrao a ON ar.atividade_id = a.id
                ORDER BY ar.data DESC
            """)
            registros = cursor.fetchall()
            conexao.close()
#Abaixo nós apagamos os registros do visor, para que não fique igual o excell cheio de coisas abertas
            texto_resultado.delete("1.0", tk.END)
            texto_resultado.insert(tk.END, f"{'Nome'.ljust(20)}{'Atividade'.ljust(25)}{'Data'.ljust(12)}{'Horas'}\n")
            texto_resultado.insert(tk.END, "-"*65 + "\n")
            for r in registros:
                texto_resultado.insert(
                tk.END,
                f"{r[0].ljust(20)}{r[1].ljust(25)}{str(r[2]).ljust(12)}{str(r[3]) + 'h'}\n"
                )
    def gerar_relatorio():
        conexao = conectar()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute("""
                SELECT u.nome, SUM(ar.horas) as total_horas
                FROM atividades_realizadas ar
                JOIN usuarios u ON ar.usuario_id = u.id
                GROUP BY u.nome
                ORDER BY total_horas DESC;
            """)
            relatorio = cursor.fetchall()
            conexao.close()

            texto_resultado.delete("1.0", tk.END)
            texto_resultado.insert(tk.END, "RELATÓRIO - Total de Horas por Bolsista\n\n")
            for r in relatorio:
                texto_resultado.insert(tk.END, f"{r[0]} - {r[1]} horas\n")

    btn_carregar = tk.Button(admin_janela, text="Carregar Registros", command=carregar_registros)
    btn_carregar.pack(pady=5)

    btn_relatorio = tk.Button(admin_janela, text="Gerar Relatório", command=gerar_relatorio)
    btn_relatorio.pack(pady=5)

    pass