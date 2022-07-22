from interfaces.profissional import Profissional

class Barbeiro(Profissional):
    def __init__(self, servico: str) -> None:
        self.servico = servico

    def get_servico(self) -> str:
        tipoProfissional = self.servico
        if tipoProfissional == "":
            return "corte de Cabelo" 
        elif tipoProfissional == "Barbeiro":
            return "corte de Cabelo Estilizado" 
        
    def get_extra(self) -> str:
        extra = self.servico
        if extra == "Barbeiro":
            return "barba"
        else:
            return ""
        