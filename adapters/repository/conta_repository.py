from domain.interfaces.repositories import IContaRepository
from domain.entities.conta import Conta
from sqlalchemy.orm import Session
from sqlalchemy import insert, select

class ContaRepository(IContaRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_account(self, account: Conta) -> Conta:
        try:
            self.session.add(
                Conta(
                    holder=account.holder,
                    balance=account.balance
                )
            )
            self.session.commit()
            return account
        except Exception as e:
            raise e

    def get_account_by_id(self, account_id: int) -> Conta:
        try:
            stmt = select(Conta).where(Conta.id==account_id)
            account = self.session.scalar(stmt)
            return account
        except Exception as e:
            raise e