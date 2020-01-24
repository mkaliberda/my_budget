from datetime import datetime
from sqlalchemy import Integer, Column, String, DateTime
from app import db  # noqa


class Transaction(db.Model):  # type: ignore
    """A snazzy Widget"""

    __tablename__ = "transaction"

    id = Column(Integer(), primary_key=True)
    pub_date = Column(DateTime(), nullable=False, default=datetime.utcnow)
    amount = Column(Integer(), nullable=False, default=0)