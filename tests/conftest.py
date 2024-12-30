import pytest

from domain.entities.entity import Base


@pytest.fixture(scope="function")
def session():
    Base.metadata.create_all(engine)
    try:
        with Session() as session:
            yield session
    finally:
        Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def seed(session):
    session.add_all(
        [
            User(id=1, fullname="John Doe"),
            User(id=2, fullname="Katarine Alex"),
        ]
    )
    session.commit()