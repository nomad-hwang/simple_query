
from abc import ABCMeta, abstractmethod
from typing import Dict, List

class DatabaseInterface(metaclass=ABCMeta):
    @property
    @abstractmethod
    def connected(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def connect(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def disconnect(self) -> None:
        raise NotImplementedError()

    @abstractmethod
    def query(self, query: str, *args, **kwargs) -> List[Dict]:
        raise NotImplementedError()
