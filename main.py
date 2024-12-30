# from fastapi import FastAPI, HTTPException
# from application.services.check_balance import CheckBalanceService
# from adapters.repository.conta_memory_repository import ContaMemoryRepository
# from infrastructure.logging.logging_config import setup_logging
# import logging

# setup_logging()
# logger = logging.getLogger(__name__)

# app = FastAPI(title="Finanças Clean Architecture", version="1.0.0")

# conta_memory_repository = ContaMemoryRepository()

# @app.on_event("startup")
# async def startup_event():
#     logger.info("Iniciando aplicação...")

# @app.get("/contas/{account_id}/saldo", summary="Consulta o saldo de uma conta")
# def check_balance(account_id: int):
#     logger.info(f"Recebida solicitação de saldo para a conta {account_id}")
#     service = CheckBalanceService(conta_memory_repository)
#     try:
#         balance = service.execute(account_id)
#         logger.info(f"Saldo consultado para conta {account_id}: {balance}")
#         return {"conta_id": account_id, "saldo": balance}
#     except Exception as e:
#         logger.error(f"Erro ao consultar saldo para conta {account_id}: {e}", exc_info=True)
#         raise HTTPException(status_code=404, detail=str(e))

# @app.on_event("shutdown")
# def shutdown_event():
#     logger.info("Finalizando aplicação...")

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from application.services.check_balance import CheckBalanceService
from adapters.repository.conta_memory_repository import ContaMemoryRepository
from adapters.repository.conta_repository import ContaRepository
from application.services.conta_service import ContaService
from infrastructure.logging.logging_config import setup_logging
from domain.entities.conta import Conta
from domain.dtos.conta_dto import ContaRequest
import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

setup_logging()
logger = logging.getLogger(__name__)

engine = create_engine("postgresql+psycopg2://postgres:root@127.0.0.1:5432/bank")

session = Session(engine)

conta_repository = ContaRepository(session)
conta_service = ContaService(conta_repository)

app = FastAPI(title="Finanças Clean Architecture", version="1.0.0")

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

conta_memory_repository = ContaMemoryRepository()

@app.on_event("startup")
async def startup_event():
    logger.info("Iniciando aplicação...")

@app.get("/contas/{account_id}/saldo", summary="Consulta o saldo de uma conta")
def check_balance(account_id: int):
    logger.info(f"Recebida solicitação de saldo para a conta {account_id}")
    service = CheckBalanceService(conta_memory_repository)
    try:
        balance = service.execute(account_id)
        logger.info(f"Saldo consultado para conta {account_id}: {balance}")
        return {"conta_id": account_id, "saldo": balance}
    except Exception as e:
        logger.error(f"Erro ao consultar saldo para conta {account_id}: {e}", exc_info=True)
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/contas", summary="Cria uma nova conta")
async def create_account(account_req: ContaRequest):
    logger.info(f"Recebida solicitação para criação de conta no nome de {account_req.holder}")
    account = account_req.MapContaRequest()
    account_created = conta_service.create_account(account)
    logger.info("Conta criada com sucesso")
    return {"conta": account}

@app.on_event("shutdown")
def shutdown_event():
    logger.info("Finalizando aplicação...")

# def app():
#     with engine.connect() as conn:
#         stmt = text("select * from pg_database")
#         print(conn.execute(stmt).fetchall())


# if __name__ == "__main__":
#     app()

