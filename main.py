#import json
#import logging
from typing import List
from src.service.listaProjetosService import getProjetosService, getProjetosByUserService, getProjetosByIdService
from src.service.cadastraProjetoService import criaProjetoService


#https://realpython.com/python-type-checking/


class Main:

    param = True

    def __init__(self) -> None:
        pass

    def listaProjetos():
        projetos = getProjetosService()

        return projetos

    def criaProjeto(projeto:List):
        print("Cria Projeto: ", projeto)
        projeto = criaProjetoService(projeto)

        return projeto




#print(Main.listaProjetos())

obj = {
    "nome_projeto": "Projeto Foreign Key - 33", 
    "descricao_projeto": "Descricao do Projeto - 33", 
    "funcional_inclusao": "000000333", 
    "data_inclusao": '2022-01-15 00:56:51', 
    "funcional_manutencao": "000000333", 
    "data_inclusao_manutencao": '2022-01-15 00:56:51 ', 
    "situacao_registro": 1, 
    "diretorio_projeto": "/repo-2", 
    "grupo_acesso": "2", 
    "tipo_ambiente": 2, 
    "usuario_execucao": "executaHQL-33"
    }


print(Main.criaProjeto(obj))