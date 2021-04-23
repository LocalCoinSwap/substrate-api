from substrateutils import Kusama
from substrateutils import Polkadot
from substrateutils import update_registry

from .settings import ARBITRATOR_KEY
from .settings import KUSAMA_NODE_PROVIDER
from .settings import POLKADOT_NODE_PROVIDER

update_registry()
print("Kusama provider", KUSAMA_NODE_PROVIDER)
print("Polkadot provider", POLKADOT_NODE_PROVIDER)

kusama = Kusama(arbitrator_key=ARBITRATOR_KEY, node_url=KUSAMA_NODE_PROVIDER)
kusama.connect()

polkadot = Polkadot(arbitrator_key=ARBITRATOR_KEY, node_url=POLKADOT_NODE_PROVIDER)
polkadot.connect()

print("Kusama runtime", kusama.runtime_info()["specVersion"])
print("Polkadot runtime", polkadot.runtime_info()["specVersion"])

CHAIN_MAP = {
    "KSM": kusama,
    "DOT": polkadot,
}
