# Modulo que faz a interacao com o Banco
# Modulo para interacao com o banco de dados

from typing import List, Set, Dict, Tuple, Optional
from ...db.dbConnect import conexao
from ..mapper.Projeto import CadastraProjeto as mapperProjeto


class CadastraProjeto:


    def __init__(self, projeto: Dict) -> None:
        Session = conexao()
        self.session = Session()
        
        self.session.add(mapperProjeto(projeto))
        self.session.commit()
        #self.itens = projeto
        #print("Validar os itens: ", projeto)


    def cadastrar(self, obj_projeto: Dict) -> Tuple:

        try:

            self.session.add(mapperProjeto)
            self.commit()
        except Exception as e:
            print("Erro no Insert: ", e.__str__)

        return True

        # stmt = insert(projeto).values(projeto.id_projeto = obj_projeto.id_projeto)
        #
        # result = session.execute(q).all()
        # print(result)
        # for id in result:
        #     print(id)
        # return id







