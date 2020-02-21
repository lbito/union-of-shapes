from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def update_params(self): pass
    
    @abstractmethod
    def render(self): pass