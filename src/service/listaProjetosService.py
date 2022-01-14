# Modulo com as Regras de Negocio

from typing import List, Set, Dict, Tuple, Optional
from ..model.repository.listaProjetoRepository import getProjetos, getProjetosByUser, getProjetosById


def getProjetosService() -> List[List[dict]]:
    return getProjetos()


def getProjetosByUserService(user: str) -> List[dict]:
    print("user", user)
    rst = getProjetosByUser(user)
    return retornoListaProjetos(rst)


def getProjetosByIdService(id: int) -> List[dict]:
    return getProjetosById(id)


def retornoListaProjetos(lista: List[Tuple]) -> List:
    arr = list(lista[0])
    return arr


