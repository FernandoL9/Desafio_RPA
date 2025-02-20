import pandas as pd
import os 
from sqlalchemy import create_engine

def save_data_excel(db_name='database/savebooks.db', file_name = 'data_extracting/save_excel_extracting_data.xlsx' ):
   os.makedirs('data_extracting', exist_ok=True ) # Criando a pasta data_extracting caso não exista
   engine = create_engine(f'sqlite:///{db_name}')# Caminho do Banco de Dados
   query = 'SELECT title, price, availability FROM savebooks' 
   df = pd.read_sql_query(query, engine) # Lendo os dados do Banco de Dados
   df.to_excel(file_name, index=False) # Salvando os dados em um arquivo Excel
   print(f'Relatório gerado com sucesso em {file_name}') 