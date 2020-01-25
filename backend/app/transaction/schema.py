import marshmallow as ma
from .model import TransactionType
from marshmallow_enum import EnumField

class TransactionSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    pub_date = ma.fields.DateTime()
    amount = ma.fields.Number()
    precision = ma.fields.Integer()
    tx_type = EnumField(TransactionType)