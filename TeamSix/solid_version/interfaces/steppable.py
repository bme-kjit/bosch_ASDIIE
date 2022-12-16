import abc

class Steppable(abc.ABC):
    """
    Interface for elements depending on timing
    """
    @abc.abstractmethod
    def step(self):
        """
        Advances one step
        @return:
        """
        pass
