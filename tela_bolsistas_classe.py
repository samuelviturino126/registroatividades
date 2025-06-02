import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import *
from conectar import conectar
from datetime import datetime
from pathlib import Path
from tkinter import messagebox
import psycopg2



class TelaBolsista():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        #CAMINHOS
        #TEXTOS
        #CAIXAS
        #COMBOBOXES
        #BOTÕES
    def selecionar_atividades(self):
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
            SELECT ap.nome
            FROM atividade_por_usuarios AS au
            JOIN atividades_padrao AS ap ON au.atividade_id = ap.id
            WHERE au.usuario_id = %s;
        """, (self.id))
        self.dados = cursor.fetchall()
        for nome in self.dados:
            print(nome[0])
    def atividades_do_dia_bolsista(self):
        pass




