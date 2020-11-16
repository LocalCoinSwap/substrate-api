from substrateutils import Kusama
from substrateutils import Polkadot

from .settings import ARBITRATOR_KEY
from .settings import KUSAMA_NODE_PROVIDER
from .settings import POLKADOT_NODE_PROVIDER

print("Kusama provider", KUSAMA_NODE_PROVIDER)
print("Polkadot provider", POLKADOT_NODE_PROVIDER)

kusama = Kusama(arbitrator_key=ARBITRATOR_KEY, node_url=KUSAMA_NODE_PROVIDER)
kusama.connect()

polkadot = Polkadot(arbitrator_key=ARBITRATOR_KEY, node_url=POLKADOT_NODE_PROVIDER)
polkadot.connect()

print("Kusama runtime", kusama.runtime_info()["specVersion"])
print("Polkadot runtime", polkadot.runtime_info()["specVersion"])


def load_substrate_types(args):
    currency = args.get("currency") if args.get("currency", None) else "kusama"
    if currency == "kusama":
        kusama.load_type_registry()
    if currency == "polkadot":
        polkadot.load_type_registry()
