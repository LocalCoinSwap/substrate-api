from flask_restful import reqparse
from flask_restful import Resource

from .logger import Logger
from .middleware import kusama

# from ksmutils.helper import sign_payload

# use 'Api:class_name' as extra.namespace tag
log = Logger("Api", True, True, False)
log.info("Loading API....")

GETBALANCE = [{"name": "address", "type": str, "required": True}]

GETNONCE = [{"name": "address", "type": str, "required": True}]

# GETEVENTS = [{"name": "block_hash", "type": str, "required": True}]

GETEXTRINSICHASH = [{"name": "final_transaction", "type": str, "required": True}]

GETEXTRINSICTIMEPOINT = [
    {"name": "node_response", "type": str, "required": True},
    {"name": "final_transaction", "type": str, "required": True},
]

GETEXTRINSICEVENTS = [
    {"name": "block_hash", "type": str, "required": True},
    {"name": "extrinsinc_index", "type": int, "required": True},
]

GETESCROWADDRESS = [
    {"name": "buyer_address", "type": str, "required": True},
    {"name": "seller_address", "type": str, "required": True},
    {"name": "threshold", "type": int, "required": False},
]

GETBLOCKHASH = [{"name": "node_response", "type": str, "required": True}]

TRANSFERPAYLOAD = [
    {"name": "from_address", "type": str, "required": True},
    {"name": "to_address", "type": str, "required": True},
    {"name": "value", "type": int, "required": True},
]

APPROVEASMULTIPAYLOAD = [
    {"name": "from_address", "type": str, "required": True},
    {"name": "to_address", "type": str, "required": True},
    {"name": "value", "type": int, "required": True},
    {"name": "other_signatories", "type": list, "required": True},
]

ASMULTIPAYLOAD = [
    {"name": "from_address", "type": str, "required": True},
    {"name": "to_address", "type": str, "required": True},
    {"name": "value", "type": int, "required": True},
    {"name": "other_signatories", "type": list, "required": True},
    {"name": "timepoint", "type": tuple, "required": False},
]

ESCROWPAYLOADS = [
    {"name": "seller_address", "type": str, "required": True},
    {"name": "escrow_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "fee_value", "type": int, "required": True},
]

RELEASEESCROW = [
    {"name": "buyer_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "other_signatories", "type": list, "required": True},
    {"name": "timepoint", "type": tuple, "required": True},
]

CANCELLATION = [
    {"name": "seller_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "fee_value", "type": int, "required": True},
    {"name": "other_signatories", "type": list, "required": True},
    {"name": "timepoint", "type": tuple, "required": True},
]

RESOLVEDISPUTE = [
    {"name": "victor", "type": str, "required": True},
    {"name": "seller_address", "type": str, "required": True},
    {"name": "trade_value", "type": int, "required": True},
    {"name": "fee_value", "type": int, "required": True},
    {"name": "other_signatories", "type": list, "required": True},
    {"name": "welfare_value", "type": tuple, "required": False},
]

ISTRANSACTIONSUCCESS = [
    {"name": "transaction_type", "type": str, "required": True},
    {"name": "events", "type": list, "required": True},
]

PUBLISH = [
    {"name": "type", "type": str, "required": True},
    {"name": "params", "type": list, "required": True},
]

BROADCAST = [
    {"name": "type", "type": str, "required": True},
    {"name": "transaction", "type": str, "required": True},
]

DIAGNOSE = [{"name": "escrow_address", "type": str, "required": True}]


class GetBalance(Resource):
    """
    Returns the free balance associated with provided address
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for parameter in GETBALANCE:
            self.reqparse.add_argument(
                parameter["name"],
                type=parameter["type"],
                required=parameter["required"],
                action="store",
            )
        super(GetBalance, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        address = args["address"]

        return kusama.get_balance(address)


class GetNonce(Resource):
    """
    Returns the free balance associated with provided address
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for parameter in GETNONCE:
            self.reqparse.add_argument(
                parameter["name"],
                type=parameter["type"],
                required=parameter["required"],
                action="store",
            )
        super(GetNonce, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        address = args["address"]

        return kusama.get_nonce(address)


class GetExtrinsicHash(Resource):
    """
    Returns the extrinsic hash from provided final transaction
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for parameter in GETEXTRINSICHASH:
            self.reqparse.add_argument(
                parameter["name"],
                type=parameter["type"],
                required=parameter["required"],
                action="store",
            )
        super(GetExtrinsicHash, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        final_transaction = args["final_transaction"]

        return kusama.get_extrinsic_hash(final_transaction)


class GetExtrinsicTimepoint(Resource):
    """
    Returns the extrinsic timepoint from provided final transaction
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for parameter in GETEXTRINSICTIMEPOINT:
            self.reqparse.add_argument(
                parameter["name"],
                type=parameter["type"],
                required=parameter["required"],
                action="store",
            )
        super(GetExtrinsicTimepoint, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        final_transaction = args["final_transaction"]
        node_response = args["node_response"]
        return kusama.get_extrinsic_timepoint(node_response, final_transaction)


class GetExtrinsicEvents(Resource):
    """
    Returns the extrinsic timepoint from provided final transaction
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for parameter in GETEXTRINSICEVENTS:
            self.reqparse.add_argument(
                parameter["name"],
                type=parameter["type"],
                required=parameter["required"],
                action="store",
            )
        super(GetExtrinsicEvents, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        block_hash = args["block_hash"]
        extrinsinc_index = args["extrinsinc_index"]
        return kusama.get_extrinsic_events(block_hash, extrinsinc_index)


class GetEscrowAddress(Resource):
    """
    Returns the extrinsic timepoint from provided final transaction
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for parameter in GETESCROWADDRESS:
            self.reqparse.add_argument(
                parameter["name"],
                type=parameter["type"],
                required=parameter["required"],
                action="store",
            )
        super(GetEscrowAddress, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        buyer_address = args["buyer_address"]
        seller_address = args["seller_address"]

        return kusama.get_escrow_address(buyer_address, seller_address)


class GetBlockHash(Resource):
    """
    Returns the extrinsic timepoint from provided final transaction
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for parameter in GETBLOCKHASH:
            self.reqparse.add_argument(
                parameter["name"],
                type=parameter["type"],
                required=parameter["required"],
                action="store",
            )
        super(GetBlockHash, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        node_response = args["node_response"]

        return kusama.get_block_hash(node_response)


class TransferPayload(Resource):
    """
    Returns the extrinsic timepoint from provided final transaction
    """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for parameter in TRANSFERPAYLOAD:
            self.reqparse.add_argument(
                parameter["name"],
                type=parameter["type"],
                required=parameter["required"],
                action="store",
            )
        super(TransferPayload, self).__init__()

    def post(self):
        args = self.reqparse.parse_args()
        from_address = args["from_address"]
        to_address = args["to_address"]
        value = args["value"]

        return kusama.transfer_payload(from_address, to_address, value)


class HeartBeat(Resource):
    """
    Are we alive?
    """

    def get(self):
        return True


def get_resources(api):
    api.add_resource(HeartBeat, "/HeartBeat")
    api.add_resource(GetBalance, "/GetBalance")
    api.add_resource(GetNonce, "/GetNonce")
    api.add_resource(GetExtrinsicHash, "/GetExtrinsicHash")
    api.add_resource(GetExtrinsicTimepoint, "/GetExtrinsicTimepoint")
    api.add_resource(GetExtrinsicEvents, "/GetExtrinsicEvents")
    api.add_resource(GetEscrowAddress, "/GetEscrowAddress")
    api.add_resource(GetBlockHash, "/GetBlockHash")
    api.add_resource(TransferPayload, "/TransferPayload")
