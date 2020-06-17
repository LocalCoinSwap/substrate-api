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
        payload = {}
        response = test_client.post("/TransferPayload", json=payload).get_json()
        assert not response


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
        payload = {}
        response = test_client.post("/EscrowPayloads", json=payload).get_json()
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


class TestApproveAsMultiPayload:
    def test_endpoint(self, test_client):
        payload = {}
        response = test_client.post("/ApproveAsMultiPayload", json=payload).get_json()
        assert not response


class TestReleaseEscrow:
    def test_endpoint(self, test_client):
        payload = {}
        response = test_client.post("/ReleaseEscrow", json=payload).get_json()
        assert not response


class TestCancellation:
    def test_endpoint(self, test_client):
        payload = {}
        response = test_client.post("/Cancellation", json=payload).get_json()
        assert not response


class TestDispute:
    def test_endpoint(self, test_client):
        payload = {}
        response = test_client.post("/Dispute", json=payload).get_json()
        assert not response


class TestIsTransactionSuccess:
    def test_endpoint(self, test_client):
        payload = {}
        response = test_client.post("/IsTransactionSuccess", json=payload).get_json()
        assert not response


class TestDiagnose:
    def test_endpoint(self, test_client):
        payload = {}
        response = test_client.post("/Diagnose", json=payload).get_json()
        assert not response