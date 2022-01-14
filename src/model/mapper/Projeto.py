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
    #tipo_ambiente = Column('cod_tipo_ambi_exeo', Integer, ForeignKey(TipoAmbiente.id_tipo_ambiente))
    tipo_ambiente = Column('cod_tipo_ambi_exeo', Integer, ForeignKey('tbfs4011_tipo_ambi_exeo.cod_tipo_ambi_exeo'))
    usuario_execucao = Column('nom_usua_exeo_prjt', String(60), nullable=False )

    def __init__(self, objProjeto: dict) -> None:
        self.nome_projeto = objProjeto['nome_projeto'],
        self.descricao_projeto = objProjeto['descricao_projeto'],
        self.funcional_inclusao = objProjeto['funcional_inclusao'],
        self.data_inclusao = objProjeto['data_inclusao'],
        self.funcional_manutencao = objProjeto['funcional_manutencao'],
        self.data_inclusao_manutencao = objProjeto['data_inclusao_manutencao'],
        self.situacao_registro = objProjeto['situacao_registro'],
        self.diretorio_projeto = objProjeto['diretorio_projeto'],
        self.grupo_acesso = objProjeto['grupo_acesso'],
        self.tipo_ambiente = objProjeto['tipo_ambiente'],
        self.usuario_execucao = objProjeto['usuario_execucao']

        

class TipoAmbiente(Base):
    __tablename__ = 'tbfs4011_tipo_ambi_exeo'

    id_tipo_ambiente = Column('cod_tipo_ambi_exeo', Integer, nullable=False, primary_key=True)
    nome_tipo_ambiente = Column('nom_tipo_ambi_exeo', String(50), nullable=False, unique=True)




