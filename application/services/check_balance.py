from domain.interfaces.repositories import IContaRepository
from isNullOrEmpty.is_null_or_empty import is_null_or_empty

class CheckBalanceService:
    def __init__(self, repository: IContaRepository):
        self.repository = repository

    def execute(self, conta_id: int) -> float:
        conta = self.repository.get_account_by_id(conta_id)
        if is_null_or_empty(conta):
            raise Exception("Conta não encontrada.")
        return conta.balance