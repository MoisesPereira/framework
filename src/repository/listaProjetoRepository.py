# Modulo que faz a interacao com o Banco
# Modulo para interacao com o banco de dados

from typing import List, Set, Dict, Tuple, Optional

from ..db.dbConnect import conexao
from ..mapper.TipoAmbiente import TipoAmbiente
from ..mapper.CadastraProjeto import CadastraProjeto as projeto


Session = conexao()
session = Session()


def getProjetos() -> List[Tuple]:

    q = session.query(projeto.nome_projeto)

    result = session.execute(q).all()
    print(result)
    for id in result:
        print(id)
    return id


def getProjetosByUser(user: str) -> List[Tuple]:

    q = session.query(projeto.id_projeto, projeto.nome_projeto).filter(projeto.usuario_execucao == user).all()
    print("primeiro retorno: ", q)
    return q


def getProjetosById(id_projeto: int) -> List[Tuple]:

    q = session.query(projeto.nome_projeto).filter(projeto.id_projeto == id_projeto)

    result = session.execute(q).all()
    for id in result:
        print(id)        

    return id
