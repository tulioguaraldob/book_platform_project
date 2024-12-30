from domain.interfaces.repositories import IContaRepository
from domain.entities.conta import Conta

class ContaService:
    def __init__(self, conta_repository: IContaRepository):
        self.conta_repository = conta_repository

    def create_account(self, account: Conta) -> Conta:
        return self.conta_repository.create_account(account)
