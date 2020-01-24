
from .model import Transaction 
from .schema import  TransactionSchema

BASE_ROUTE=''

def register_routes(api, root_location):
    from .controller import tx_blueprint
    api.register_blueprint(tx_blueprint, url_prefix=f"{root_location}{tx_blueprint.url_prefix}")