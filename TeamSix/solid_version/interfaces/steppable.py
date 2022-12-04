import abc

class Steppable(abc.ABC):
    @abc.abstractmethod
    def step(self):
        pass
