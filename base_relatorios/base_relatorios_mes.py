#aqui vamos iniciar a base dos nossos relatórios
#relatório por data
from datetime import datetime
from conectar import conectar
def intervalo_mes(mes_ano):
    """
    Retorna o primeiro dia e o primeiro dia do mês seguinte (início e fim do intervalo)
    Ex: '07/2025' → (datetime(2025, 7, 1), datetime(2025, 8, 1))
    """
    try:
        inicio = datetime.strptime("01/" + mes_ano, "%d/%m/%Y")
        if inicio.month == 12:
            proximo_mes = datetime(inicio.year + 1, 1, 1)
        else:
            proximo_mes = datetime(inicio.year, inicio.month + 1, 1)
    except ValueError:
        raise ValueError("Formato de data inválido. Use MM/YYYY.")

    return inicio, proximo_mes
def obter_total_por_setor(setor, mes_ano):
    conexao = conectar()
    cursor = conexao.cursor()
    inicio, proximo_mes = intervalo_mes(mes_ano)
    #soma as quantidades por setor
    cursor.execute("""SELECT SUM(inteiro) FROM atividades_realizadas
                   WHERE setor = %s
                   AND data >= %s
                   AND data < %s""", (setor, inicio, proximo_mes))
    total = cursor.fetchone()[0]
    conexao.close()
    total = int(total)
    if total is None:
        total = 0
    return total
def obter_atividades_por_setor(setor):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""Select id FROM atividades_padrao WHERE setor = %s""", (setor,))
    atividades = cursor.fetchall()
    conexao.close()
    return atividades
def obter_total_por_atividade(atividade_id, mes_ano):
    conexao = conectar()
    cursor = conexao.cursor()
    inicio, proximo_mes = intervalo_mes(mes_ano)
        # Busca o nome da atividade
    cursor.execute("""
        SELECT nome FROM atividades_padrao WHERE id = %s
    """, (atividade_id,))
    resultado = cursor.fetchone()
    if not resultado:
        return ("Atividade não encontrada", 0)
    nome_atividade = resultado[0]
    # Soma as quantidades do mês
    cursor.execute("""
        SELECT SUM(inteiro) FROM atividades_realizadas
        WHERE atividade_id = %s
            AND data >= %s
            AND data < %s
    """, (atividade_id, inicio, proximo_mes))
    total = cursor.fetchone()[0]
    conexao.close()
    total = int(total)
    if total is None:
        total = 0

    return nome_atividade, total
#abaixo um exemplo para buscar a atividade catalogação
mesano = ("06/2025")
print(obter_total_por_atividade(1, mesano))

def total_por_mes(mes_ano):
    conexao = conectar()
    cursor = conexao.cursor()
    inicio, proximo_mes = intervalo_mes(mes_ano)
    #Soma as quantidades do mês
    cursor.execute("""
                   SELECT SUM(inteiro) FROM atividades_realizadas
                   WHERE data >= %s
                   AND data < %s
                   """, (inicio, proximo_mes))
    total = cursor.fetchone()[0]
    conexao.close()
    total = int(total)
    if total is None:
        total = 0
    return total
print(total_por_mes(mesano))

def comparar_porcentagem(valor, total):
    #obtem o valor da porcentagem sem o % do lado
    if total == 0:
        return 0  # evita divisão por zero
    porcentagem = (valor / total) * 100
    return round(porcentagem, 2)  # arredonda para 2 casas decimais

def porcentagem_por_setor(setor, mes_ano):
    total_geral = obter_total_por_setor(setor, mes_ano)
    atividades = obter_atividades_por_setor(setor)
    resultado = []
    conexao = conectar()
    cursor = conexao.cursor()
    inicio, proximo_mes = intervalo_mes(mes_ano)
    for atividade in atividades:
        atividade_id = atividade[0]  # fetchall retorna lista de tuplas
        # Obtem o total dessa atividade específica
        cursor.execute("""
            SELECT SUM(inteiro) FROM atividades_realizadas
            WHERE setor = %s AND atividade_id = %s
              AND data >= %s AND data < %s
        """, (setor, atividade_id, inicio, proximo_mes))
        subtotal = cursor.fetchone()[0]
        if subtotal is None:
            subtotal = 0
        # Calcula a porcentagem
        porcentagem = comparar_porcentagem(subtotal, total_geral)
        # Armazena a tupla na lista
        if subtotal > 0:
            resultado.append((atividade_id, porcentagem))

    conexao.close()
    return resultado

print(porcentagem_por_setor("Processamento Técnico", "06/2025"))

