import marshmallow as ma

class TransactionSchema(ma.Schema):
    id = ma.fields.Int(dump_only=True)
    pub_date = ma.fields.DateTime()
    amount = ma.fields.Integer()