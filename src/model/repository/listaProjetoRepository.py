# Modulo que faz a interacao com o Banco
# Modulo para interacao com o banco de dados

from typing import List, Set, Dict, Tuple, Optional

from ...db.dbConnect import conexao
#from ..mapper.TipoAmbiente import TipoAmbiente
from ..mapper.Projeto import CadastraProjeto as mapperProjeto
#from ..mapper.Projeto import TipoAmbiente as ambiente


Session = conexao()
session = Session()


def getProjetos() -> List[Tuple]:

    projetos = session.query(mapperProjeto).all()
    arrProjetos = []
    for projeto in projetos:
        dictre = dict(projeto.__dict__)
        dictre.pop('_sa_instance_state', None)
        arrProjetos.append(dictre)

    return arrProjetos

    # print(projetos)
    # for projeto in projetos:
    #     p = projeto.pop('_sa_instance_state', None)
    #     print(p.__dict__)
    # return p

    # dictret.pop('_sa_instance_state', None)


def getProjetosByUser(user: str) -> List[Tuple]:

    q = session.query(mapperProjeto.id_projeto, mapperProjeto.nome_projeto).filter(mapperProjeto.usuario_execucao == user).all()
    print("primeiro retorno: ", q)
    return q


def getProjetosById(id_projeto: int) -> List[Tuple]:

    q = session.query(mapperProjeto.nome_projeto).filter(mapperProjeto.id_projeto == id_projeto)

    result = session.execute(q).all()
    for id in result:
        print(id)        

    return id
