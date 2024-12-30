from sqlalchemy.orm import Session
from domain.entities.entity import Base
from domain.entities.conta import Conta

class TestContaRepository:
    def setup_class(self):
        Base.metadata.create_all(engine)
        self.session = Session()
        self.valid_account = Conta(
            holder="Aybak",
            balance=100
        )

    def teardown_class(self):
        self.session.rollback()
        self.session.close()

    def test_author_valid(self):   
        self.session.add(self.valid_account)
        self.session.commit()
        aybak = self.session.query(Conta).filter_by(holder="Aybak").first()
        assert aybak.balance == 100