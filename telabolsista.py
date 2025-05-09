import tkinter as tk
from tkinter import messagebox
from conectar import conectar

def abrir_tela_bolsista(usuario_id, nome_bolsista):
    janela_bolsista = tk.Toplevel()
    janela_bolsista.title(f"Bolsista: {nome_bolsista}")

    tk.Label(janela_bolsista, text=f"Olá, {nome_bolsista}!").pack(pady=5)

    # Carrega as atividades disponíveis do banco
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome FROM atividades_padrao ORDER BY nome")
    atividades = cursor.fetchall()
    conexao.close()

    # Lista de atividades
    tk.Label(janela_bolsista, text="Selecione a atividade:").pack()
    atividade_var = tk.StringVar()
    atividade_menu = tk.OptionMenu(janela_bolsista, atividade_var, *[a[1] for a in atividades])
    atividade_menu.pack()

    # Campo de horas
    tk.Label(janela_bolsista, text="Horas gastas:").pack()
    entrada_horas = tk.Entry(janela_bolsista)
    entrada_horas.pack()

    def registrar_atividade():
        nome_atividade = atividade_var.get()
        horas = entrada_horas.get()

        if not nome_atividade or not horas:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
            return

        try:
            horas = float(horas)
        except:
            messagebox.showerror("Erro", "Horas deve ser um número.")
            return

        # Busca o ID da atividade selecionada
        atividade_id = next((a[0] for a in atividades if a[1] == nome_atividade), None)

        # Salva no banco
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO atividades_realizadas (usuario_id, atividade_id, data, horas)
            VALUES (%s, %s, CURRENT_DATE, %s)
        """, (usuario_id, atividade_id, horas))
        conexao.commit()
        conexao.close()

        messagebox.showinfo("Sucesso", "Atividade registrada!")
        entrada_horas.delete(0, tk.END)

    # Botão de registrar
    tk.Button(janela_bolsista, text="Registrar Atividade", command=registrar_atividade).pack(pady=10)

    pass