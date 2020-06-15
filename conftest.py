import pytest
from flask_restful import Api

from service.api import get_resources
from service.application import create_application


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_application()
    test_client = flask_app.test_client()
    # Establish an application context during the tests.
    ctx = flask_app.app_context()
    ctx.push()
    get_resources(Api(flask_app))
    yield test_client
    ctx.pop()
