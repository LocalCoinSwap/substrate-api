class TestSanity:
    def test_sanity(self, test_client):
        """
        Test that test setup works
        """
        response = test_client.get("/HeartBeat").get_json()
        assert response


class TestBalance:
    def test_endpoint(self, test_client):
        payload = {"address": "HsgNgA5sgjuKxGUeaZPJE8rRn9RuixjvnPkVLFUYLEpj15G"}
        response = test_client.post("/Balance", json=payload).get_json()
        assert response == 22000000000


class TestNonce:
    def test_endpoint(self, test_client):
        payload = {"address": "HsgNgA5sgjuKxGUeaZPJE8rRn9RuixjvnPkVLFUYLEpj15G"}
        response = test_client.post("/Nonce", json=payload).get_json()
        assert response == 0


class TestTransferPayload:
    def test_endpoint(self, test_client):
        payload = {
            "from_address": "HsgNgA5sgjuKxGUeaZPJE8rRn9RuixjvnPkVLFUYLEpj15G",
            "to_address": "CrjrfWVeFM7CFc3fvhwA7etuTdGirnSqBBNBzTiyTcRrPsP",
            "value": 22000000000,
        }
        response = test_client.post("/TransferPayload", json=payload).get_json()
        assert len(response) == 232 and response[0:2] == "0x"


class TestEscrowAddress:
    def test_endpoint(self, test_client):
        payload = {
            "buyer_address": "DwRh5ShcnuPzgyhW6J6m4mw1y63hUy1ctR3RSWRSgLg1HQ5",
            "seller_address": "CrjrfWVeFM7CFc3fvhwA7etuTdGirnSqBBNBzTiyTcRrPsP",
        }
        response = test_client.post("/EscrowAddress", json=payload).get_json()
        assert response == "Fgh5GQ1guNxvurv71cmHm8H5Eo8Ywrdz1mZemffAP2UrrH2"


class TestEscrowPayloads:
    def test_endpoint(self, test_client):
        payload = {
            "seller_address": "D2bHQwFcQj11SvtkjULEdKhK4WAeP6MThXgosMHjW9DrmbE",
            "escrow_address": "CofvaLbP3m8PLeNRQmLVPWmTT7jGgAXTwyT69k2wkfPxJ9V",
            "trade_value": 9900000000,
            "fee_value": 100000000,
        }
        response = test_client.post("/EscrowPayloads", json=payload).get_json()
        assert (
            len(response["escrow_payload"]) == 232
            and response["escrow_payload"][0:2] == "0x"
        )
        assert (
            len(response["fee_payload"]) == 228 and response["fee_payload"][0:2] == "0x"
        )
        assert type(response["nonce"]) == int


class TestApproveAsMultiPayload:
    def test_endpoint(self, test_client):
        payload = {
            "from_address": "HsgNgA5sgjuKxGUeaZPJE8rRn9RuixjvnPkVLFUYLEpj15G",
            "to_address": "CrjrfWVeFM7CFc3fvhwA7etuTdGirnSqBBNBzTiyTcRrPsP",
            "value": 9900000000,
            "other_signatories": [
                "D2bHQwFcQj11SvtkjULEdKhK4WAeP6MThXgosMHjW9DrmbE",
                "CofvaLbP3m8PLeNRQmLVPWmTT7jGgAXTwyT69k2wkfPxJ9V",
            ],
        }
        response = test_client.post("/ApproveAsMultiPayload", json=payload).get_json()
        assert type(response["nonce"]) == int
        assert (
            len(response["approve_as_multi_payload"]) == 356
            and response["approve_as_multi_payload"][0:2] == "0x"
        )


class TestReleaseEscrow:
    def test_endpoint(self, test_client):
        payload = {
            "buyer_address": "CrjrfWVeFM7CFc3fvhwA7etuTdGirnSqBBNBzTiyTcRrPsP",
            "trade_value": 9900000000,
            "other_signatories": [
                "D2bHQwFcQj11SvtkjULEdKhK4WAeP6MThXgosMHjW9DrmbE",
                "CofvaLbP3m8PLeNRQmLVPWmTT7jGgAXTwyT69k2wkfPxJ9V",
            ],
            "timepoint": (2000, 8),
        }
        response = test_client.post("/ReleaseEscrow", json=payload).get_json()
        assert len(response) == 444 and response[0:2] == "0x"


"""
class TestCancellation:
    def test_endpoint(self, test_client):
        payload = {
            "seller_address": "",
            "trade_value": "",
            "fee_value": "",
            "other_signatories": "",
            "timepoint": "",
        }
        response = test_client.post("/Cancellation", json=payload).get_json()
        assert not response


class TestDispute:
    def test_endpoint(self, test_client):
        payload = {
            "victor": "",
            "seller_address": "",
            "trade_value": "",
            "fee_value": "",
            "other_signatories": "",
            "welfare_value": "",
        }
        response = test_client.post("/Dispute", json=payload).get_json()
        assert not response


class TestIsTransactionSuccess:
    def test_endpoint(self, test_client):
        payload = {
            "transaction_type": "",
            "events": "",
        }
        response = test_client.post("/IsTransactionSuccess", json=payload).get_json()
        assert not response


class TestDiagnose:
    def test_endpoint(self, test_client):
        payload = {
            "name": "",
        }
        response = test_client.post("/Diagnose", json=payload).get_json()
        assert not response


class TestPublish:
    def test_endpoint(self, test_client):
        payload = {}
        response = test_client.post("/Publish", json=payload).get_json()
        assert not response


class TestBroadcast:
    def test_endpoint(self, test_client):
        payload = {}
        response = test_client.post("/Broadcast", json=payload).get_json()
        assert not response

"""
