import json
import logging
from src.service.listaProjetosService import getProjetosService, getProjetosByUserService, getProjetosByIdService


def main(user, context):
    
    # CONTROLLER DA APLICAÇÃO
    # Rota que ira receber o id do usuario - Retorna os projetos atrelados ao usuario
    # Adicionar a parte de paginação
    # Rota que ira receber o id do Projeto - Retorna apenas 1 projeto

    a = getProjetosByUserService(user)
    print("VALOR A: ", a)

    b = json.dumps(a)
    print("VALOR B: ", b)

    # logging.info('I told you so', rst)

    return b

main("goiaba", None)
