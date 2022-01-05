from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy import Sequence
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()


class CadastraProjeto(Base):
    __tablename__ = 'tbfs4003_prjt_trfm_dado'

    id_projeto = Column('cod_prjt_trfm_dado', Integer, nullable=False, primary_key=True, autoincrement=True)
    nome_projeto = Column('nom_prjt_trfm_dado', String(100), nullable=False)
    descricao_projeto = Column('des_prjt_trfm_dado', String(500), nullable=False)
    funcional_inclusao = Column('num_funl_cola_cogl_incu', String(9), nullable=False)
    data_inclusao = Column('dat_hor_incu_rgto', DateTime, default=datetime.now)
    funcional_manutencao = Column('num_funl_cola_cogl_mant', String(9), nullable=False)
    data_inclusao_manutencao = Column('dat_hor_mant_rgto', DateTime, default=datetime.now)
    situacao_registro = Column('ind_situ_rgto', Integer, nullable=False)
    diretorio_projeto = Column('nom_drto_prjt', String(255), nullable=False)
    grupo_acesso = Column('cod_grup_aces', Integer, nullable=False)
    tipo_ambiente = Column('cod_tipo_ambi_exeo', Integer, nullable=False)
    usuario_execucao = Column('nom_usua_exeo_prjt', String(60), nullable=False )