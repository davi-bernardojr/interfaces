from abc import ABC, abstractmethod

class Profissional(ABC):

    @abstractmethod
    def get_servico(self) -> str:
        pass

    @abstractmethod
    def get_extra(self) -> str:
        pass

    