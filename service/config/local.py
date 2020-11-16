import os

from dotenv import load_dotenv

load_dotenv()
UNIFIED_LOGGING = False
DEBUG_STATUS = True
LOGSTASH = {"host": "localhost", "port": 9601, "name": "kusama_api_logger"}
INTERNAL_ONLY = False
PORT = 12000
HOST = "0.0.0.0"
ARBITRATOR_KEY = os.getenv("ARBITRATOR_HEX_SEED")
KUSAMA_NODE_PROVIDER = "wss://kusama-rpc.polkadot.io/"
POLKADOT_NODE_PROVIDER = "wss://rpc.polkadot.io/"
