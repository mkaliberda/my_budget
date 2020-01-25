from flask import Flask
from flask.views import MethodView
from flask_smorest import Api, Blueprint, abort
from .schema import TransactionSchema
from .model import TransactionModel, TransactionType

tx_blueprint = Blueprint("TransactionSchema",
                        "transaction",
                        url_prefix="/transactions",
                        description="transactions")

@tx_blueprint.route('/')
class TransactionView(MethodView):

    @tx_blueprint.response(TransactionSchema(many=True))
    def get(self):
        """ List """
        # TODO SHOULD PROVIDE SERVICE
        return TransactionModel.query.all()
