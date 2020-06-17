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
        response = test_client.post("/TransferPayload").get_json()
        assert not response


class TestEscrowAddress:
    def test_endpoint(self, test_client):
        response = test_client.post("/EscrowAddress").get_json()
        assert not response


class TestEscrowPayloads:
    def test_endpoint(self, test_client):
        response = test_client.post("/EscrowPayloads").get_json()
        assert not response


class TestPublish:
    def test_endpoint(self, test_client):
        response = test_client.post("/Publish").get_json()
        assert not response


class TestBroadcast:
    def test_endpoint(self, test_client):
        response = test_client.post("/Broadcast").get_json()
        assert not response


class TestApproveAsMultiPayload:
    def test_endpoint(self, test_client):
        response = test_client.post("/ApproveAsMultiPayload").get_json()
        assert not response


class TestReleaseEscrow:
    def test_endpoint(self, test_client):
        response = test_client.post("/ReleaseEscrow").get_json()
        assert not response


class TestCancellation:
    def test_endpoint(self, test_client):
        response = test_client.post("/Cancellation").get_json()
        assert not response


class TestDispute:
    def test_endpoint(self, test_client):
        response = test_client.post("/Dispute").get_json()
        assert not response


class TestIsTransactionSuccess:
    def test_endpoint(self, test_client):
        response = test_client.post("/IsTransactionSuccess").get_json()
        assert not response


class TestDiagnose:
    def test_endpoint(self, test_client):
        response = test_client.post("/Diagnose").get_json()
        assert not response
