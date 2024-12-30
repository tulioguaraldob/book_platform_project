from pydantic import BaseModel
from domain.entities.conta import Conta

class ContaRequest(BaseModel):
    holder: str
    balance: float

    def MapContaRequest(self) -> Conta:
        return Conta(holder=self.holder, balance=self.balance)
