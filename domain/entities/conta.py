from sqlalchemy import Column, DateTime, String, Float, Integer, func, Identity
from domain.entities.entity import Base

class Conta(Base):
    __tablename__ = "contas"

    id = Column(Integer, Identity(), primary_key=True)
    holder = Column(String(255), unique=False)
    balance = Column(Float)

    def __repr__(self):
        return f"id: {self.id}, holder: {self.holder}"

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance