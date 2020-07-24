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
            "other_trader": "D2bHQwFcQj11SvtkjULEdKhK4WAeP6MThXgosMHjW9DrmbE",
        }
        response = test_client.post("/ApproveAsMultiPayload", json=payload).get_json()
        assert type(response["nonce"]) == int
        assert (
            len(response["approve_as_multi_payload"]) == 372
            and response["approve_as_multi_payload"][0:2] == "0x"
        )


class TestAsMultiPayload:
    def test_endpoint(self, test_client):
        payload = {
            "from_address": "HsgNgA5sgjuKxGUeaZPJE8rRn9RuixjvnPkVLFUYLEpj15G",
            "to_address": "CrjrfWVeFM7CFc3fvhwA7etuTdGirnSqBBNBzTiyTcRrPsP",
            "value": 9900000000,
            "other_trader": "D2bHQwFcQj11SvtkjULEdKhK4WAeP6MThXgosMHjW9DrmbE",
            "timepoint": (2000, 8),
        }
        response = test_client.post("/AsMultiPayload", json=payload).get_json()
        assert type(response["nonce"]) == int
        assert (
            len(response["as_multi_payload"]) == 372
            and response["as_multi_payload"][0:2] == "0x"
        )


class TestReleaseEscrow:
    def test_endpoint(self, test_client):
        payload = {
            "buyer_address": "CrjrfWVeFM7CFc3fvhwA7etuTdGirnSqBBNBzTiyTcRrPsP",
            "trade_value": 9900000000,
            "seller_address": "D2bHQwFcQj11SvtkjULEdKhK4WAeP6MThXgosMHjW9DrmbE",
            "timepoint": (2000, 8),
        }
        response = test_client.post("/ReleaseEscrow", json=payload).get_json()
        assert len(response) == 688 and response[0:2] == "0x"


class TestCancellation:
    def test_endpoint(self, test_client):
        payload = {
            "seller_address": "CofvaLbP3m8PLeNRQmLVPWmTT7jGgAXTwyT69k2wkfPxJ9V",
            "trade_value": 9900000000,
            "fee_value": 10000,
            "buyer_address": "D2bHQwFcQj11SvtkjULEdKhK4WAeP6MThXgosMHjW9DrmbE",
            "timepoint": (2000, 8),
        }
        response = test_client.post("/Cancellation", json=payload).get_json()
        assert len(response) == 688 and response[0:2] == "0x"


class TestDispute:
    def test_endpoint(self, test_client):
        payload = {
            "victor": "buyer",
            "seller_address": "CofvaLbP3m8PLeNRQmLVPWmTT7jGgAXTwyT69k2wkfPxJ9V",
            "trade_value": 9900000000,
            "fee_value": 100000,
            "buyer_address": "D2bHQwFcQj11SvtkjULEdKhK4WAeP6MThXgosMHjW9DrmbE",
            "welfare_value": 100000,
        }
        response = test_client.post("/Dispute", json=payload).get_json()
        assert len(response) == 428 and response[0:2] == "0x"


class TestDiagnose:
    def test_endpoint(self, test_client):
        payload = {
            "escrow_address": "HFXXfXavDuKhLLBhFQTat2aaRQ5CMMw9mwswHzWi76m6iLt",
        }
        response = test_client.post("/Diagnose", json=payload).get_json()
        assert type(response) == dict
        assert response.get(
            "0cef89f69f02a6cde5169574b6474ddc8e513dbf257c6fdfbe30ebd1303c2cee", None
        )


class TestPublish:
    def test_endpoint(self, test_client, mocker):
        mocker.patch("service.middleware.kusama.publish", return_value=[True, ""])

        payload = {
            "type": "transfer",
            "params": [
                "D2bHQwFcQj11SvtkjULEdKhK4WAeP6MThXgosMHjW9DrmbE",
                "56b3f88ae9c5de73b18449b789a98087463f7d8b7fc0dac6fee4c82597e24c6fe2d0398458842eb561de49b14de2f0ddb2313d5c12de347592e96fa30d4f2480",
                34,
                "GKm5rrf151KKrMeKEo3TxqKuznnWE1uz5zGvj4ZB19uGmqE",
                10000000000,
            ],
        }
        response = test_client.post("/Publish", json=payload).get_json()
        assert response


class TestBroadcast:
    def test_endpoint(self, test_client, mocker):
        mocker.patch("service.middleware.kusama.broadcast", return_value=[True, ""])

        payload = {
            "type": "transfer",
            "transaction": "0x3502840c85dc20f15e3d8328b6a162d47ce43771fe6925f0effb8b878bcd1ff28d8f1201ea312383c4ed09954453395653a3e84f779c080c2ba80c06562047b6b882c64b171d47c7773dd82c353deddea1b4d24baa54324766ddb47d24692754b91f57850090000400dee35cf94a50737fc2f3c60439e8bae056aabdcde99de4f2d37a5f5957bcec4b0700e40b5402",
        }
        response = test_client.post("/Broadcast", json=payload).get_json()
        assert response
