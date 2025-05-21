#Aqui vamos ter nossa função para conectar ao servidor SQL por meio da API do postgreeSQL a psycopg2

import psycopg2
import os #esse import permite utilizarmos variaveis do ambiente, utilizei essa ideia para não deixar um curioso ver as infos da base de dados

def conectar():
    try: 
        conexao = psycopg2.connect( #Esse é um comando da biblioteca para se conectar com o servidor SQL
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"), #Abrindo a base de dados Registro_de_Atividades
            user=os.getenv("DB_USER"), #utiliza o de adm no SQL
            password=os.getenv("DB_SENHA")
        )
        print("Conexão sucedida")
        return conexao
    except Exception as e:
        print("Erro", e)
        return None
conectar() 