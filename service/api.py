from flask_restful import Resource

from service.logger import Logger
from service.middleware import kusama
from service.typings import approve_as_multi_payload
from service.typings import balance
from service.typings import broadcast
from service.typings import cancellation
from service.typings import diagnose
from service.typings import dispute
from service.typings import escrow_address
from service.typings import escrow_payloads
from service.typings import is_transaction_success
from service.typings import nonce
from service.typings import publish
from service.typings import release_escrow
from service.typings import transfer_payload
from service.utils import PostResource

log = Logger("Api", True, True, False)
log.info("Loading API....")


class Balance(PostResource):
    """
    Get the free balance from an address
    """

    def __init__(self):
        super(Balance, self).__init__(balance)

    def post(self):
        args = self.reqparse.parse_args()
        address = args["address"]

        return kusama.get_balance(address)


class Nonce(PostResource):
    """
    Get the nonce from an address
    """

    def __init__(self):
        super(Nonce, self).__init__(nonce)

    def post(self):
        args = self.reqparse.parse_args()
        address = args["address"]

        return kusama.get_nonce(address)


class TransferPayload(PostResource):
    """
    Get a payload to sign for a regular transfer
    """

    def __init__(self):
        super(TransferPayload, self).__init__(transfer_payload)

    def post(self):
        args = self.reqparse.parse_args()
        from_address = args["from_address"]
        to_address = args["to_address"]
        value = args["value"]

        return kusama.transfer_payload(from_address, to_address, value)


class EscrowAddress(PostResource):
    """
    Get an address to use for escrow
    """

    def __init__(self):
        super(EscrowAddress, self).__init__(escrow_address)

    def post(self):
        args = self.reqparse.parse_args()
        buyer_address = args["buyer_address"]
        seller_address = args["seller_address"]

        return kusama.get_escrow_address(buyer_address, seller_address)


class EscrowPayloads(PostResource):
    """
    Get the payloads to sign to initiate escrow
    """

    def __init__(self):
        super(EscrowPayloads, self).__init__(escrow_payloads)


class Publish(PostResource):
    """
    Build and publish a transaction
    """

    def __init__(self):
        super(Publish, self).__init__(publish)


class Broadcast(PostResource):
    """
    Broadcast a built transaction
    """

    def __init__(self):
        super(Broadcast, self).__init__(broadcast)


class ApproveAsMultiPayload(PostResource):
    """
    Get the payload to sign for an approve as multi call
    """

    def __init__(self):
        super(ApproveAsMultiPayload, self).__init__(approve_as_multi_payload)


class ReleaseEscrow(PostResource):
    """
    Get the transactions to broadcast to release escrow
    """

    def __init__(self):
        super(ReleaseEscrow, self).__init__(release_escrow)


class Cancellation(PostResource):
    """
    Get the transactions to broadcast to perform a cancellation
    """

    def __init__(self):
        super(Cancellation, self).__init__(cancellation)


class Dispute(PostResource):
    """
    Get the transactions to broadcast to resolve a dispute
    """

    def __init__(self):
        super(Dispute, self).__init__(dispute)


class IsTransactionSuccess(PostResource):
    """
    Check if a transaction was successful
    """

    def __init__(self):
        super(IsTransactionSuccess, self).__init__(is_transaction_success)


class Diagnose(PostResource):
    """
    Diagnose an escrow address from a problematic trade
    """

    def __init__(self):
        super(Diagnose, self).__init__(diagnose)


class HeartBeat(Resource):
    """
    Are we alive?
    """

    def get(self):
        return True


def get_resources(api):
    api.add_resource(Nonce, "/Nonce")
    api.add_resource(Balance, "/Balance")
    api.add_resource(TransferPayload, "/TransferPayload")
    api.add_resource(EscrowAddress, "/EscrowAddress")
    api.add_resource(EscrowPayloads, "/EscrowPayloads")
    api.add_resource(Publish, "/Publish")
    api.add_resource(Broadcast, "/Broadcast")
    api.add_resource(ApproveAsMultiPayload, "/ApproveAsMultiPayload")
    api.add_resource(ReleaseEscrow, "/ReleaseEscrow")
    api.add_resource(Cancellation, "/Cancellation")
    api.add_resource(Dispute, "/Dispute")
    api.add_resource(IsTransactionSuccess, "/IsTransactionSuccess")
    api.add_resource(Diagnose, "/Diagnose")
    api.add_resource(HeartBeat, "/HeartBeat")
