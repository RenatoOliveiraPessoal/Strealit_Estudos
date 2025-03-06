import pyodbc

# Defina o nome do DSN configurado no ODBC
dsn_name = 'DM2'  # Substitua 'FirebirdDSN' pelo nome do seu DSN
user = 'USER_READ'  # Seu usuário ODBC
password = 'USRREAD'  # Sua senha ODBC

# Conectando-se ao banco de dados via ODBC
conn = pyodbc.connect(f'DSN={dsn_name}')

# Criar um cursor para executar as consultas
cursor = conn.cursor()

# Executar uma consulta SQL
cursor.execute("""
    SELECT CHAVENFE AS CHAVE, 
           CAST(TRIM(SUBSTRING(CHAVENFE FROM 26 FOR 9)) AS INTEGER) AS NOTA,  
           CAST(DTHREMISSAO AS DATE) AS DATA_EMISSAO, 
           CNPJCPF AS CNPJ, 
           NOME AS FORNECEDOR, 
           VLRNFE AS VALOR, 
           CASE CODLANC WHEN 0 THEN 'PENDENTE' ELSE 'ENTRADA REALIZADA' END AS STATUS 
    FROM MANIFESTDEST 
    WHERE CAST(DTHREMISSAO AS DATE) >= CURRENT_DATE - 30
    AND TIPONOTA = 0 
    AND TIPO_OPERACAO = 1
""")

# Obter os resultados
rows = cursor.fetchall()

# Exibir os resultados
for row in rows:
    print(row)

# Fechar a conexão e o cursor
cursor.close()
conn.close()
