from interfaces.profissional import Profissional

class Freelancer(Profissional):
    def __init__(self, servico: str, extra: str) -> None:
        self.servico = servico
        self.extra = extra

    def get_servico(self) -> str:
        servico = self.servico
        return servico
    
    def get_extra(self) -> str:
        extra = self.extra        
        return extra