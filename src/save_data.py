import pandas as pd
import os 
from sqlalchemy import create_engine

def save_data_sqlite(data, db_name='database/savebooks.db' ):
   
   os.makedirs( "database", exist_ok=True ) # Criando a pasta database caso não exista
   db_path = os.path.abspath( db_name ) # Caminho do Banco de Dados
   engine = create_engine(f'sqlite:///{db_path}') # Criando o Banco de Dados
   df = pd.DataFrame(data) # Convertendo os dados em um DataFrame

   df.to_sql('savebooks', engine, if_exists='replace', index=False) # Salvando no Banco de Dados
   print('Dados salvos com sucesso!')
   