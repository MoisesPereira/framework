from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

def conexao():

    user = os.getenv('USER') + ":"
    pwd = os.getenv('PSWD') + "@"
    host = os.getenv('HOST') + "/"
    database = os.getenv('DATABASE')
    strConn = "mysql+pymysql://" + user + pwd + host + database

    engine = create_engine(strConn, echo=True)

    return sessionmaker(bind=engine)