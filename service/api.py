from flask_restful import Resource

from service import typings
from service.logger import Logger
from service.middleware import CHAIN_MAP
from service.utils import PostResource

log = Logger("Api", True, True, False)
log.info("Loading API....")


class BasePostResource(PostResource):
    def chain(self):
        args = self.reqparse.parse_args()
        currency = args.get("currency", "KSM")
        chain = CHAIN_MAP[currency]
        return chain


class Balance(BasePostResource):
    """
    Get the free balance from an address
    """

    def __init__(self):
        super(Balance, self).__init__(typings.balance)

    def post(self):
        args = self.reqparse.parse_args()
        return self.chain().get_balance(args["address"])


class MultiBalance(BasePostResource):
    """
    Get the balances from an address dictionary
    """

    def __init__(self):
        super(MultiBalance, self).__init__(typings.multi_balance)

    def post(self):
        args = self.reqparse.parse_args()
        currency = args.get("currency", "KSM")

        addresses = args["addresses"]
        result = {}

        for address in addresses:
            result[address] = {currency: {}}
            result[address][currency]["amount"] = self.chain().get_balance(address)

        return result


class Nonce(BasePostResource):
    """
    Get the nonce from an address
    """

    def __init__(self):
        super(Nonce, self).__init__(typings.nonce)

    def post(self):
        args = self.reqparse.parse_args()
        return self.chain().get_nonce(args["address"])


class TransferPayload(BasePostResource):
    """
    Get a payload to sign for a regular transfer
    """

    def __init__(self):
        super(TransferPayload, self).__init__(typings.transfer_payload)

    def post(self):
        args = self.reqparse.parse_args()
        return self.chain().transfer_payload(
            args["from_address"], args["to_address"], args["value"]
        )


class EscrowAddress(BasePostResource):
    """
    Get an address to use for escrow
    """

    def __init__(self):
        super(EscrowAddress, self).__init__(typings.escrow_address)

    def post(self):
        args = self.reqparse.parse_args()
        return self.chain().get_escrow_address(
            args["buyer_address"], args["seller_address"]
        )


class EscrowPayloads(BasePostResource):
    """
    Get the payloads to sign to initiate escrow
    """

    def __init__(self):
        super(EscrowPayloads, self).__init__(typings.escrow_payloads)

    def post(self):
        args = self.reqparse.parse_args()

        escrow_payload, fee_payload, nonce = self.chain().escrow_payloads(
            args["seller_address"],
            args["escrow_address"],
            args["trade_value"],
            args["fee_value"],
        )

        return {
            "escrow_payload": escrow_payload,
            "fee_payload": fee_payload,
            "nonce": nonce,
        }


class AsMultiPayload(BasePostResource):
    """
    Get the payload to sign for an as multi call
    """

    def __init__(self):
        super(AsMultiPayload, self).__init__(typings.as_multi_payload)

    def post(self):
        args = self.reqparse.parse_args()

        address = self.chain().arbitrator_address
        store_call = args["store_call"] if args["store_call"] else False
        max_weight = args["max_weight"] if args["max_weight"] else 648378000

        as_multi_payload, nonce = self.chain().as_multi_payload(
            args["from_address"],
            args["to_address"],
            args["value"],
            [args["other_trader"], address],
            args["timepoint"],
            store_call,
            max_weight,
        )

        return {
            "as_multi_payload": as_multi_payload,
            "nonce": nonce,
        }


class Dispute(BasePostResource):
    """
    Get the transactions to broadcast to resolve a dispute
    """

    def __init__(self):
        super(Dispute, self).__init__(typings.dispute)

    def post(self):
        args = self.reqparse.parse_args()

        address = self.chain().arbitrator_address

        return self.chain().resolve_dispute(
            args["victor"],
            args["seller_address"],
            args["trade_value"],
            args["fee_value"],
            [args["buyer_address"], address],
            args["welfare_value"],
        )


class Diagnose(BasePostResource):
    """
    Diagnose an escrow address from a problematic trade
    """

    def __init__(self):
        super(Diagnose, self).__init__(typings.diagnose)

    def post(self):
        args = self.reqparse.parse_args()

        return self.chain().diagnose(args["escrow_address"])


class Publish(BasePostResource):
    """
    Build and publish a transaction
    """

    def __init__(self):
        super(Publish, self).__init__(typings.publish)

    def post(self):
        args = self.reqparse.parse_args()

        params = args["params"]
        tx_type = args["type"]

        success, response = self.chain().publish(tx_type, params)

        return {
            "success": success,
            "response": response,
        }


class PublishAsMulti(BasePostResource):
    """
    Publish `as_multi` transaction
    """

    def __init__(self):
        super(PublishAsMulti, self).__init__(typings.publish_as_multi)

    def post(self):
        args = self.reqparse.parse_args()

        max_weight = args["max_weight"] if args["max_weight"] else 648378000

        params = [
            args["from_address"],
            args["signature"],
            args["nonce"],
            args["to_address"],
            args["trade_value"],
            args["timepoint"],
            [args["other_signatory"], self.chain().arbitrator_address],
            max_weight,
        ]

        success, response = self.chain().publish("as_multi", params)

        return {
            "success": success,
            "response": response,
        }


class Broadcast(BasePostResource):
    """
    Broadcast a built transaction
    """

    def __init__(self):
        super(Broadcast, self).__init__(typings.broadcast)

    def post(self):
        args = self.reqparse.parse_args()

        success, response = self.chain().broadcast(args["type"], args["transaction"])

        return {
            "success": success,
            "response": response,
        }


class FeeReturnTx(BasePostResource):
    """
    Return the fee to the seller
    """

    def __init__(self):
        super(FeeReturnTx, self).__init__(typings.fee_return_tx)

    def post(self):
        args = self.reqparse.parse_args()

        transaction = self.chain().fee_return_transaction(
            args["seller_address"], args["trade_value"], args["fee_value"],
        )

        return {"transaction": transaction}


class WelfareTx(BasePostResource):
    """
    Give the poor buyer some funds to finish that trade
    """

    def __init__(self):
        super(WelfareTx, self).__init__(typings.welfare_tx)

    def post(self):
        args = self.reqparse.parse_args()

        transaction = self.chain().welfare_transaction(args["buyer_address"])

        return {"transaction": transaction}


class AsMultiStorage(BasePostResource):
    """
    Generate and return transaction for `as_multi` call with store=True
    """

    def __init__(self):
        super(AsMultiStorage, self).__init__(typings.as_multi_storage)

    def post(self):
        args = self.reqparse.parse_args()

        transaction = self.chain().as_multi_storage(
            args["from_address"], args["to_address"], args["value"],
        )

        return {
            "transaction": transaction,
        }


class HeartBeat(Resource):
    """
    Are we alive?
    """

    def get(self):
        return True


class SentryTest(Resource):
    """
    Test sentry error capturing
    """

    def get(self):
        _ = 4 / 0


def get_resources(api):
    api.add_resource(Nonce, "/Nonce")
    api.add_resource(Balance, "/Balance")
    api.add_resource(MultiBalance, "/AddressBalance")
    api.add_resource(TransferPayload, "/TransferPayload")
    api.add_resource(EscrowAddress, "/EscrowAddress")
    api.add_resource(EscrowPayloads, "/EscrowPayloads")
    api.add_resource(Publish, "/Publish")
    api.add_resource(PublishAsMulti, "/PublishAsMulti")
    api.add_resource(Broadcast, "/Broadcast")
    api.add_resource(AsMultiPayload, "/AsMultiPayload")
    api.add_resource(Dispute, "/Dispute")
    api.add_resource(Diagnose, "/Diagnose")
    api.add_resource(FeeReturnTx, "/FeeReturnTx")
    api.add_resource(WelfareTx, "/WelfareTx")
    api.add_resource(HeartBeat, "/HeartBeat")
    api.add_resource(AsMultiStorage, "/AsMultiStorage")
    api.add_resource(SentryTest, "/SentryTest")
