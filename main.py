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
    "nome_projeto": "6666 Projeto Foreign Key - 666", 
    "descricao_projeto": "666 Descricao do Projeto - 666", 
    "funcional_inclusao": "6666666", 
    "data_inclusao": '2022-01-15 00:56:51', 
    "funcional_manutencao": "666666666", 
    "data_inclusao_manutencao": '2022-01-15 00:56:51 ', 
    "situacao_registro": 1, 
    "diretorio_projeto": "/repo-44", 
    "grupo_acesso": "2", 
    "tipo_ambiente": 2, 
    "usuario_execucao": "666666-executaHQL-666"
    }


print(Main.criaProjeto(obj))