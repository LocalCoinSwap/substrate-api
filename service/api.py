from flask_restful import Resource

from service import typings
from service.logger import Logger
from service.middleware import kusama
from service.middleware import load_substrate_types
from service.utils import PostResource

log = Logger("Api", True, True, False)
log.info("Loading API....")


class Balance(PostResource):
    """
    Get the free balance from an address
    """

    def __init__(self):
        super(Balance, self).__init__(typings.balance)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        return kusama.get_balance(args["address"])


class MultiBalance(PostResource):
    """
    Get the balances from an address dictionary
    """

    def __init__(self):
        super(MultiBalance, self).__init__(typings.multi_balance)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        addresses = args()["addresses"]
        result = {}

        for address in addresses:
            result[address] = {"KSM": {}}
            result[address]["KSM"]["amount"] = kusama.get_balance(address)

        return result


class Nonce(PostResource):
    """
    Get the nonce from an address
    """

    def __init__(self):
        super(Nonce, self).__init__(typings.nonce)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        return kusama.get_nonce(args["address"])


class TransferPayload(PostResource):
    """
    Get a payload to sign for a regular transfer
    """

    def __init__(self):
        super(TransferPayload, self).__init__(typings.transfer_payload)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        return kusama.transfer_payload(
            args["from_address"], args["to_address"], args["value"]
        )


class EscrowAddress(PostResource):
    """
    Get an address to use for escrow
    """

    def __init__(self):
        super(EscrowAddress, self).__init__(typings.escrow_address)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        return kusama.get_escrow_address(args["buyer_address"], args["seller_address"])


class EscrowPayloads(PostResource):
    """
    Get the payloads to sign to initiate escrow
    """

    def __init__(self):
        super(EscrowPayloads, self).__init__(typings.escrow_payloads)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        escrow_payload, fee_payload, nonce = kusama.escrow_payloads(
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


class ApproveAsMultiPayload(PostResource):
    """
    Get the payload to sign for an approve as multi call
    """

    def __init__(self):
        super(ApproveAsMultiPayload, self).__init__(typings.approve_as_multi_payload)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        address = kusama.arbitrator_address

        approve_as_multi_payload, nonce = kusama.approve_as_multi_payload(
            args["from_address"],
            args["to_address"],
            args["value"],
            [args["other_trader"], address],
        )

        return {
            "approve_as_multi_payload": approve_as_multi_payload,
            "nonce": nonce,
        }


class AsMultiPayload(PostResource):
    """
    Get the payload to sign for an as multi call
    """

    def __init__(self):
        super(AsMultiPayload, self).__init__(typings.as_multi_payload)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        address = kusama.arbitrator_address
        store_call = args["store_call"] if args["store_call"] else False
        max_weight = args["max_weight"] if args["max_weight"] else 648378000

        as_multi_payload, nonce = kusama.as_multi_payload(
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


class ReleaseEscrow(PostResource):
    """
    Get the transactions to broadcast to release escrow
    """

    def __init__(self):
        super(ReleaseEscrow, self).__init__(typings.release_escrow)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        address = kusama.arbitrator_address

        return kusama.release_escrow(
            args["buyer_address"],
            args["trade_value"],
            args["timepoint"],
            [args["seller_address"], address],
        )


class Cancellation(PostResource):
    """
    Get the transactions to broadcast to perform a cancellation
    """

    def __init__(self):
        super(Cancellation, self).__init__(typings.cancellation)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        address = kusama.arbitrator_address

        return kusama.cancellation(
            args["seller_address"],
            args["trade_value"],
            args["fee_value"],
            [args["buyer_address"], address],
            args["timepoint"],
        )


class Dispute(PostResource):
    """
    Get the transactions to broadcast to resolve a dispute
    """

    def __init__(self):
        super(Dispute, self).__init__(typings.dispute)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        address = kusama.arbitrator_address

        return kusama.resolve_dispute(
            args["victor"],
            args["seller_address"],
            args["trade_value"],
            args["fee_value"],
            [args["buyer_address"], address],
            args["welfare_value"],
        )


class Diagnose(PostResource):
    """
    Diagnose an escrow address from a problematic trade
    """

    def __init__(self):
        super(Diagnose, self).__init__(typings.diagnose)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        return kusama.diagnose(args["escrow_address"])


class Publish(PostResource):
    """
    Build and publish a transaction
    """

    def __init__(self):
        super(Publish, self).__init__(typings.publish)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        params = args()["params"]
        tx_type = args()["type"]

        success, response = kusama.publish(tx_type, params)

        return {
            "success": success,
            "response": response,
        }


class PublishApproveAsMulti(PostResource):
    """
    Publish `approve_as_multi` transaction
    """

    def __init__(self):
        super(PublishApproveAsMulti, self).__init__(typings.publish_approve_as_multi)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        params = [
            args["seller_address"],
            args["signed_approve_as_multi"],
            args["approve_as_multi_nonce"],
            args["buyer_address"],
            args["trade_value"],
            [args["buyer_address"], kusama.arbitrator_address],
        ]

        success, response = kusama.publish("approve_as_multi", params)

        return {
            "success": success,
            "response": response,
        }


class PublishAsMulti(PostResource):
    """
    Publish `as_multi` transaction
    """

    def __init__(self):
        super(PublishAsMulti, self).__init__(typings.publish_as_multi)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        max_weight = args["max_weight"] if args["max_weight"] else 648378000

        params = [
            args["from_address"],
            args["signature"],
            args["nonce"],
            args["to_address"],
            args["trade_value"],
            args["timepoint"],
            [args["other_signatory"], kusama.arbitrator_address],
            max_weight,
        ]

        success, response = kusama.publish("as_multi", params)

        return {
            "success": success,
            "response": response,
        }


class Broadcast(PostResource):
    """
    Broadcast a built transaction
    """

    def __init__(self):
        super(Broadcast, self).__init__(typings.broadcast)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        success, response = kusama.broadcast(args["type"], args["transaction"])

        return {
            "success": success,
            "response": response,
        }


class FeeReturnTx(PostResource):
    """
    Return the fee to the seller
    """

    def __init__(self):
        super(FeeReturnTx, self).__init__(typings.fee_return_tx)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        transaction = kusama.fee_return_transaction(
            args["seller_address"], args["trade_value"], args["fee_value"],
        )

        return {"transaction": transaction}


class WelfareTx(PostResource):
    """
    Give the poor buyer some funds to finish that trade
    """

    def __init__(self):
        super(WelfareTx, self).__init__(typings.welfare_tx)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        transaction = kusama.welfare_transaction(args["buyer_address"])

        return {"transaction": transaction}


class AsMultiStorage(PostResource):
    """
    Generate and return transaction for `as_multi` call with store=True
    """

    def __init__(self):
        super(AsMultiStorage, self).__init__(typings.as_multi_storage)

    def post(self):
        args = self.reqparse.parse_args()
        load_substrate_types(args)

        transaction = kusama.as_multi_storage(
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
        _ = 3 / 0


def get_resources(api):
    api.add_resource(Nonce, "/Nonce")
    api.add_resource(Balance, "/Balance")
    api.add_resource(MultiBalance, "/AddressBalance")
    api.add_resource(TransferPayload, "/TransferPayload")
    api.add_resource(EscrowAddress, "/EscrowAddress")
    api.add_resource(EscrowPayloads, "/EscrowPayloads")
    api.add_resource(Publish, "/Publish")
    api.add_resource(PublishApproveAsMulti, "/PublishApproveAsMulti")
    api.add_resource(PublishAsMulti, "/PublishAsMulti")
    api.add_resource(Broadcast, "/Broadcast")
    api.add_resource(AsMultiPayload, "/AsMultiPayload")
    api.add_resource(ApproveAsMultiPayload, "/ApproveAsMultiPayload")
    api.add_resource(ReleaseEscrow, "/ReleaseEscrow")
    api.add_resource(Cancellation, "/Cancellation")
    api.add_resource(Dispute, "/Dispute")
    api.add_resource(Diagnose, "/Diagnose")
    api.add_resource(FeeReturnTx, "/FeeReturnTx")
    api.add_resource(WelfareTx, "/WelfareTx")
    api.add_resource(HeartBeat, "/HeartBeat")
    api.add_resource(AsMultiStorage, "/AsMultiStorage")
    api.add_resource(SentryTest, "/SentryTest")
