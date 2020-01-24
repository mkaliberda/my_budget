def register_routes_api_v1(api, root_location="/api/v1"):
    """
       register_blueprint api v1 group
    """
    from .transaction import register_routes as attach_transaction

    attach_transaction(api, root_location)


