from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import Sequence
from datetime import datetime

Base = declarative_base()

class TipoAmbiente(Base):
    __tablename__ = 'tbfs4011_tipo_ambi_exeo'

    id_tipo_ambiente = Column('cod_tipo_ambi_exeo', Integer, Sequence('cod_tipo_ambi_exeo'), nullable=False, primary_key=True)
    nome_tipo_ambiente = Column('nom_tipo_ambi_exeo', String(50), nullable=False, unique=True)
