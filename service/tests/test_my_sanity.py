class TestSanity:
    def test_sanity(self, test_client):
        """
        Test that test setup works
        """
        response = test_client.get("/HeartBeat").get_json()
        assert response
