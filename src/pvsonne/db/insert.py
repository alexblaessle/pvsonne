import pandas as pd
from sqlalchemy import create_engine 
from sqlalchemy.exc import SQLAlchemyError



conn_str="postgresql://alex:@localhost:5432/postgres"

engine = create_engine(conn_str)

df=pd.read_csv("test.csv").head(1)
df=df.drop(columns=["Unnamed: 0","ic_status"])
df.columns=df.columns.str.lower()

df.to_sql(     
   'data',      
   con=engine,      
   if_exists='append',      
   index=False 
)