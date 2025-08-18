from conectar import conectar

def obter_nome(usuario_id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT nome FROM usuarios WHERE id = %s", (usuario_id,))
    nome = cursor.fetchone()
    conexao.close()
    if nome:
        return str(nome[0])
    else:
        return "Usuário não encontrado"
    

def total_de_atividades_por_usuario(usuario_id, inicio, fim):
    conexao = conectar()
    cursor = conexao.cursor()
    #soma as quantidades por setor
    cursor.execute("""SELECT SUM(inteiro) FROM atividades_realizadas
                   WHERE usuario_id = %s
                   AND data >= %s
                   AND data <= %s""", (usuario_id, inicio, fim))
    total = int(cursor.fetchone()[0])
    conexao.close()
    return total

nome = obter_nome(2)
total = total_de_atividades_por_usuario(2, "02/05/2025", "02/07/2025")
print(f"{nome} fez: {total} atividades")

def obter_lista_id_de_atividades_por_usuario(usuario_id, inicio, fim):
    conexao = conectar()
    cursor = conexao.cursor()
    #distinct nao repete
    cursor.execute("""SELECT DISTINCT atividade_id FROM atividades_realizadas
                   WHERE usuario_id = %s
                   AND data >= %s
                   AND data <= %s""", (usuario_id, inicio, fim))
    atividades = cursor.fetchall()
    conexao.close()
    return [a[0] for a in atividades]

print(obter_lista_id_de_atividades_por_usuario(2, "02/05/2025", "02/07/2025"))