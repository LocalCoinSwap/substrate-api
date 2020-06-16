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

GETEVENTS = [{"name": "block_hash", "type": str, "required": True}]

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

        result = kusama.get_balance(address)
        return result


class HeartBeat(Resource):
    """
    Are we alive?
    """

    def get(self):
        return True


def get_resources(api):
    api.add_resource(HeartBeat, "/HeartBeat")
