from domain.entities.conta import Conta
from domain.interfaces.repositories import IContaRepository

class ContaMemoryRepository(IContaRepository):
    def get_account_by_id(self, account_id: int) -> Conta:
        return Conta(account_id,"Thiago Adriano", 100.0)

    def create_account(self, account: Conta) -> Conta:
        return Conta(account_id,"Thiago Adriano", 100.0)