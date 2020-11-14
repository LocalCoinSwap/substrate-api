import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

from .common import get_parameters

AWS_REGION = "us-east-1"
AWS_PARAMETER_PATH = "/prod/kusama/"

params = get_parameters(AWS_REGION, AWS_PARAMETER_PATH)

sentry_sdk.init(
    dsn=params["SENTRY_DSN"], integrations=[FlaskIntegration()], traces_sample_rate=1.0
)

app = Flask(__name__)


UNIFIED_LOGGING = False
DEBUG_STATUS = True
LOGSTASH = {"host": "localhost", "port": 9601, "name": "kusama_api_logger"}
INTERNAL_ONLY = False
PORT = 443
HOST = "0.0.0.0"
ARBITRATOR_KEY = params["ARBITRATOR_HEX_SEED"]
KUSAMA_NODE_PROVIDER = "ws://ksmnode.lcs.internal/"
POLKADOT_NODE_PROVIDER = "wss://rpc.polkadot.io/"
