from abc import ABC, abstractmethod
from domain.entities.conta import Conta

class IContaRepository(ABC):
    @abstractmethod
    def get_account_by_id(self, account_id: int):
        pass

    @abstractmethod
    def create_account(self, account: Conta):
        pass