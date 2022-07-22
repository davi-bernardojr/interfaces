from typing import Type
from interfaces.profissional import Profissional

class Trabalhador:

    def __init__(self, nome: str) -> None:
        self.nome = nome
    
    def servicoPrestado(self, servico: Type[Profissional]):
        trabalho = servico.get_servico()
        print("{} presta serviço de {}".format(self.nome, trabalho))

    def servicoExtra(self, servico: Type[Profissional]):
        extra = servico.get_extra()
        if extra == "":
            print("{} não presta outros serviços.".format(self.nome))
        else:
            print("{} também faz {}".format(self.nome, extra))