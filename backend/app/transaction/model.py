from enum import Enum, unique
from datetime import datetime
from sqlalchemy import (Integer, Column, String,
                        DateTime, ForeignKey, Numeric)
from sqlalchemy import Enum as SlqEnum
from app import db

@unique
class TransactionType(Enum):
    spend = "spend"
    income = "income"

class TransactionModel(db.Model):  # type: ignore
    """
        Model of transaction
    """

    __tablename__ = "transaction"

    id = Column(Integer(), primary_key=True)
    pub_date = Column(DateTime(), nullable=False, default=datetime.utcnow)
    amount = Column(Numeric(precision=2, scale=10), nullable=False, default=0)
    tx_type = Column(
        SlqEnum(TransactionType), nullable=False, server_default=TransactionType.spend.value
    )