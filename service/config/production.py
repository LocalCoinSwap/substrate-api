from .common import get_parameters

AWS_REGION = "us-east-1"
AWS_PARAMETER_PATH = "/prod/kusama/"

params = get_parameters(AWS_REGION, AWS_PARAMETER_PATH)

UNIFIED_LOGGING = False
DEBUG_STATUS = True
LOGSTASH = {"host": "localhost", "port": 9601, "name": "kusama_api_logger"}
INTERNAL_ONLY = False
PORT = 443
HOST = "0.0.0.0"
ARBITRATOR_KEY = params["ARBITRATOR_HEX_SEED"]
NODE_PROVIDER = "wss://kusama-rpc.polkadot.io/"
