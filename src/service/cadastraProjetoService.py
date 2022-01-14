# Modulo com as Regras de Negocio

from typing import List, Set, Dict, Tuple, Optional
from ..model.repository.cadastraProjetoRepository import CadastraProjeto


def criaProjetoService(projeto: Dict) -> List:

    print("Projeto Service: ", projeto)

    rst = CadastraProjeto(projeto)
    print("OBJETO CADASTRADO: ", rst)
    return rst
